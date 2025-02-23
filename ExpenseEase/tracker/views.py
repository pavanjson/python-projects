# views.py
import xlwt
import io
import calendar
from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense, Category, Budget, RecurringExpense
from .forms import ExpenseForm, BudgetForm
from django.db.models import Sum
from django.contrib import messages
from datetime import date, timedelta, datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from collections import defaultdict
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def dashboard(request):
    if request.user.is_authenticated:
        # Filter expenses and budgets for the logged-in user
        expenses = Expense.objects.filter(user=request.user).order_by('-date')
        total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0
        budgets = Budget.objects.filter(user=request.user)
        context = {
            'expenses': expenses,
            'total_expenses': total_expenses,
            'budgets': budgets,
        }
        return render(request, 'tracker/dashboard.html', context)
    else:
        return render(request, 'tracker/public.html')

def expense_list(request):
    if request.user.is_authenticated:
        expenses = Expense.objects.filter(user=request.user).order_by('-date')
        return render(request, 'tracker/expense_list.html', {'expenses': expenses})
    else:
        return render(request, 'tracker/public.html')

def add_expense(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ExpenseForm(request.POST)
            if form.is_valid():
                expense = form.save(commit=False)
                expense.user = request.user  # assign logged-in user
                expense.save()
                messages.success(request, 'Expense added successfully.')
                return redirect('expense_list')
        else:
            form = ExpenseForm()
        return render(request, 'tracker/expense_form.html', {'form': form, 'action': 'Add'})
    else:
        return render(request, 'tracker/public.html')

def edit_expense(request, expense_id):
    if request.user.is_authenticated:
        expense = get_object_or_404(Expense, pk=expense_id, user=request.user)
        if request.method == 'POST':
            form = ExpenseForm(request.POST, instance=expense)
            if form.is_valid():
                form.save()
                messages.success(request, 'Expense updated successfully.')
                return redirect('expense_list')
        else:
            form = ExpenseForm(instance=expense)
        return render(request, 'tracker/expense_form.html', {'form': form, 'action': 'Edit'})
    else:
        return render(request, 'tracker/public.html')

def delete_expense(request, expense_id):
    if request.user.is_authenticated:
        expense = get_object_or_404(Expense, pk=expense_id, user=request.user)
        if request.method == 'POST':
            expense.delete()
            messages.success(request, 'Expense deleted successfully.')
            return redirect('expense_list')
        return render(request, 'tracker/confirm_delete.html', {'expense': expense})
    else:
        return render(request, 'tracker/public.html')

def add_budget(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BudgetForm(request.POST)
            if form.is_valid():
                budget = form.save(commit=False)
                budget.user = request.user  # assign logged-in user
                budget.save()
                messages.success(request, 'Budget added successfully.')
                return redirect('dashboard')
        else:
            form = BudgetForm()
        return render(request, 'tracker/budget_form.html', {'form': form, 'action': 'Add'})
    else:
        return render(request, 'tracker/public.html')


def report(request):
    if request.user.is_authenticated:
        expenses = Expense.objects.filter(user=request.user)

        # Group expenses by "YYYY-MM" and then by category
        monthly_report = defaultdict(lambda: defaultdict(float))
        for expense in expenses:
            month_str = expense.date.strftime("%Y-%m")  # e.g. "2025-02"
            cat_name = expense.category.name if expense.category else "Uncategorized"
            monthly_report[month_str][cat_name] += float(expense.amount)

        # Build a list of dicts: [{month: "2025-02", categories: [...]}, ...]
        report_data = []
        for month_str, cat_data in monthly_report.items():
            categories = [
                {'category': c, 'total': t}
                for c, t in cat_data.items()
            ]
            report_data.append({'month': month_str, 'categories': categories})

        # Sort in descending order so the current/recent month is first
        # "YYYY-MM" as a string sorts correctly for ascending/descending
        report_data.sort(key=lambda x: x['month'], reverse=True)

        context = {'report_data': report_data}
        return render(request, 'tracker/report.html', context)
    else:
        return render(request, 'tracker/public.html')


def process_recurring_expenses():
    """
    Process recurring expenses for all users.
    Note: This function is not tied to a request and can be run as a scheduled task.
    """
    today = date.today()
    recurring_expenses = RecurringExpense.objects.filter(next_occurrence__lte=today)
    for rec in recurring_expenses:
        # Create a new expense based on the recurring expense template and assign the same user
        Expense.objects.create(
            user=rec.user,
            title=rec.expense.title,
            amount=rec.expense.amount,
            currency=rec.expense.currency,
            category=rec.expense.category,
            date=today,
            description=rec.expense.description,
        )
        # Update next_occurrence based on the recurrence interval
        if rec.recurrence_interval == 'daily':
            rec.next_occurrence += timedelta(days=1)
        elif rec.recurrence_interval == 'weekly':
            rec.next_occurrence += timedelta(weeks=1)
        elif rec.recurrence_interval == 'monthly':
            # Simplistic monthly increment; for production use, consider dateutil.relativedelta
            new_month = rec.next_occurrence.month % 12 + 1
            rec.next_occurrence = rec.next_occurrence.replace(month=new_month)
        elif rec.recurrence_interval == 'yearly':
            rec.next_occurrence = rec.next_occurrence.replace(year=rec.next_occurrence.year + 1)
        rec.save()

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})




def export_month_pdf(request, month):
    """
    Export the given YYYY-MM month's expenses (for the logged-in user) as a PDF.
    """
    if not request.user.is_authenticated:
        return redirect('login')

    # Parse "YYYY-MM"
    year, mon = map(int, month.split('-'))

    # Filter expenses for that month & user
    expenses = Expense.objects.filter(
        user=request.user,
        date__year=year,
        date__month=mon
    )

    # Aggregate totals by category
    monthly_summary = defaultdict(float)
    for e in expenses:
        cat_name = e.category.name if e.category else "Uncategorized"
        monthly_summary[cat_name] += float(e.amount)

    # Create a PDF in memory
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Title
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, 750, f"Expense Report for {month}")

    # Content
    y = 720
    p.setFont("Helvetica", 12)
    for cat, total in monthly_summary.items():
        p.drawString(50, y, f"{cat}: {total}")
        y -= 20

    p.showPage()
    p.save()
    buffer.seek(0)

    # Return PDF as response
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="report_{month}.pdf"'
    return response



def export_month_excel(request, month):
    """
    Export the given YYYY-MM month's expenses (for the logged-in user) as an Excel file.
    """
    if not request.user.is_authenticated:
        return redirect('login')

    year, mon = map(int, month.split('-'))
    expenses = Expense.objects.filter(
        user=request.user,
        date__year=year,
        date__month=mon
    )

    monthly_summary = defaultdict(float)
    for e in expenses:
        cat_name = e.category.name if e.category else "Uncategorized"
        monthly_summary[cat_name] += float(e.amount)

    # Create a workbook in memory
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Monthly Report')

    # Title row
    ws.write(0, 0, f"Expense Report for {month}")

    # Headers
    row = 2
    ws.write(row, 0, "Category")
    ws.write(row, 1, "Total Amount")
    row += 1

    # Write category totals
    for cat, total in monthly_summary.items():
        ws.write(row, 0, cat)
        ws.write(row, 1, total)
        row += 1

    # Return as Excel
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="report_{month}.xls"'
    wb.save(response)
    return response
