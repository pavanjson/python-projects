# Import necessary modules from Django
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Import Task model from the current directory
from .models import Task

# Custom login view
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    # Redirect to tasks page after successful login
    def get_success_url(self):
        return reverse_lazy('tasks')

# Custom user creation form with additional fields
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    # Save the additional fields to the user model
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

# Registration page view
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    # Log in the user after successful registration
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    # Redirect to tasks page if user is already authenticated
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)

# Task list view
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    # Filter tasks by user and search input
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        context['search_input'] = search_input

        # Add the count for each status type
        context['todo_count'] = context['tasks'].filter(status='todo').count()
        context['started_count'] = context['tasks'].filter(status='started').count()
        context['completed_count'] = context['tasks'].filter(status='complete').count()
        context['archived_count'] = context['tasks'].filter(status='archived').count()

        return context

# Task detail view
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

# Task creation view
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'base/task_create.html'
    success_url = reverse_lazy('tasks')
    form_class = forms.modelform_factory(model, fields=['title', 'description', 'status', 'due'], 
                                         widgets={'due': forms.DateTimeInput(attrs={'type': 'datetime-local'})})

    # Set the task's user to the current user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)

# Task update view
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'base/task_update.html'
    success_url = reverse_lazy('tasks')
    form_class = forms.modelform_factory(Task, fields=['title', 'description', 'status', 'due'], 
                                         widgets={'due': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
                                                  'description': CKEditorWidget()})

# Task deletion view
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task_delete.html'
    success_url = reverse_lazy('tasks')