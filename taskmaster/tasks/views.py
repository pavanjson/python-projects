from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from datetime import date
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login



@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def task_detail(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})


@login_required
def task_create(request):
    today = date.today()  # Get today's date

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {'form': form, 'today': today})


@login_required
def task_update(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    today = date.today()  # Get today's date

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form, 'today': today})


@login_required
def task_delete(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


def home(request):
    return render(request, 'tasks/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')  # redirect after successful registration
        else:
            print(form.errors)  # Check form errors in the console
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list')
        else:
            print(form.errors)  # Ensure errors are being printed in the console
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
