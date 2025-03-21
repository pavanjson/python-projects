from .forms import ContactForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project
from .forms import ProjectForm
from django.db.models import Q

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form (e.g., send email or store message)
            messages.success(request, "Thank you for your message!")
            return redirect('contact')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'core/contact.html', context)


def portfolio(request):
    if request.user.is_authenticated:
        projects = Project.objects.filter(
            Q(published=True) | Q(created_by=request.user)
        ).order_by('-created_at')
    else:
        projects = Project.objects.filter(published=True).order_by('-created_at')
    context = {'projects': projects}
    return render(request, 'core/portfolio.html', context)


@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            messages.success(request, "Project created successfully!")
            return redirect('portfolio')
    else:
        form = ProjectForm()
    return render(request, 'core/create_project.html', {'form': form})

@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.user != project.created_by:
        messages.error(request, "You are not authorized to edit this project.")
        return redirect('portfolio')
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project updated successfully!")
            return redirect('portfolio')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'core/edit_project.html', {'form': form, 'project': project})

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.user != project.created_by:
        messages.error(request, "You are not authorized to delete this project.")
        return redirect('portfolio')
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project deleted successfully!")
        return redirect('portfolio')
    return render(request, 'core/confirm_project_delete.html', {'project': project})

@login_required
def toggle_project_publish(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.user != project.created_by:
        messages.error(request, "You are not authorized to change this project’s publish status.")
        return redirect('portfolio')
    project.published = not project.published
    project.save()
    messages.success(request, "Project status updated successfully!")
    return redirect('portfolio')
