from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Book, Transaction
from .forms import BookForm, TransactionForm, UserRegistrationForm
from django.contrib import messages
from datetime import timedelta


def home(request):
    return render(request, 'home.html')


@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})


@user_passes_test(lambda u: u.is_superuser)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/book_form.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'library/book_confirm_delete.html', {'book': book})


@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'library/transaction_list.html', {'transactions': transactions})


@login_required
def request_rent_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id, num_available__gt=0)
    existing_request = Transaction.objects.filter(user=request.user, book=book, status='Pending')

    if existing_request.exists():
        messages.info(request, 'You already have a pending request for this book.')
    else:
        Transaction.objects.create(user=request.user, book=book, status='Pending')
        messages.success(request, 'Your rental request has been submitted.')

    return redirect('transaction_list')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def is_admin(user):
    return user.is_superuser


@user_passes_test(is_admin)
def manage_requests(request):
    pending_requests = Transaction.objects.filter(status__in=['Pending', 'Approved', 'Issued'])
    return render(request, 'library/manage_requests.html', {'pending_requests': pending_requests})


@user_passes_test(is_admin)
def approve_request(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id, status='Pending')
    if request.method == 'POST':
        transaction.status = 'Approved'
        transaction.save()
        messages.success(request, 'Request approved.')
    return redirect('manage_requests')


@user_passes_test(is_admin)
def deny_request(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id, status='Pending')
    if request.method == 'POST':
        transaction.status = 'Denied'
        transaction.save()
        messages.info(request, 'Request denied.')
    return redirect('manage_requests')


@user_passes_test(is_admin)
def issue_book_admin(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id, status='Approved')

    if request.method == 'POST':
        due_date = request.POST.get('due_date')

        transaction.issue_date = timezone.now().date()
        transaction.due_date = due_date
        transaction.status = 'Issued'

        transaction.book.num_available -= 1
        transaction.book.save()

        transaction.save()
        messages.success(request, f'Book issued to {transaction.user.username}.')
        return redirect('manage_requests')

    return render(request, 'library/admin_issue_book.html', {'transaction': transaction})


@login_required
def request_early_return(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id, user=request.user, status='Issued')
    transaction.status = 'ReturnRequested'
    transaction.save()
    messages.success(request, 'Early return requested.')
    return redirect('transaction_list')


@user_passes_test(is_admin)
def manage_return_requests(request):
    return_requests = Transaction.objects.filter(status='ReturnRequested')
    return render(request, 'library/manage_return_requests.html', {'return_requests': return_requests})


@user_passes_test(is_admin)
def update_return(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id, status='ReturnRequested')

    if request.method == 'POST':
        transaction.return_date = timezone.now().date()
        transaction.status = 'Returned'

        transaction.book.num_available += 1
        transaction.book.save()

        if transaction.return_date > transaction.due_date:
            days_late = (transaction.return_date - transaction.due_date).days
            transaction.late_fee = days_late * 1.00

        transaction.save()
        messages.success(request, f'Return confirmed for "{transaction.book.title}".')
        return redirect('manage_return_requests')