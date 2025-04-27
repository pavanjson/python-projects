# PortfolioPro/apps/core/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

from .models import Project, Profile
from .forms import ProjectForm, ProfileForm, ContactForm, CustomUserCreationForm
from apps.blog.models import Post

from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings

# --- Auth Views ---

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = AuthenticationForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        return form


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Create empty profile
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'core/register.html', {'form': form})


# --- Public Views ---

def home(request):
    users = User.objects.all().order_by('username')  # Fetch all users sorted by username
    return render(request, 'core/home.html', {'users': users})


def user_profile(request, username):
    user = get_object_or_404(User, username=username)

    # Fetch published projects
    projects = Project.objects.filter(created_by=user, published=True).order_by('-created_at')

    # Fetch published blog posts
    posts = Post.objects.filter(author=user).order_by('-published_date')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f"New Contact from {sender_name}"
            full_message = f"You have received a new message from {sender_name} ({sender_email}):\n\n{message}"
            print("subject: ", subject)
            print("full message: ", full_message)
            # Send email
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,  # from your app email
                [user.email],                  # to user’s registered email
                fail_silently=False,
            )

            messages.success(request, "✅ Your message has been sent successfully!")
            return redirect('user_profile', username=user.username)
    else:
        form = ContactForm()

    context = {
        'user': user,
        'projects': projects,
        'posts': posts,
        'form': form,
    }
    return render(request, 'core/user_profile.html', context)

def about(request, username):
    user = get_object_or_404(User, username=username)
    # Fetch published projects
    projects = Project.objects.filter(created_by=user, published=True).order_by('-created_at')

    # Fetch published blog posts
    posts = Post.objects.filter(author=user).order_by('-published_date')
    form = ContactForm()

    context = {
        'user': user,
        'projects': projects,
        'posts': posts,
        'form': form,
    }
    return render(request, 'core/user_profile.html', context)



def contact(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f"New Contact from {sender_name}"
            full_message = f"You have received a new message from {sender_name} ({sender_email}):\n\n{message}"

            # Send email to the profile user's registered email
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,  # From email (your app email)
                [user.email],                  # To email (profile user's email)
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect('user_profile', username=user.username)
    else:
        form = ContactForm()

    context = {'form': form, 'user': user}
    return render(request, 'core/contact.html', context)



def portfolio(request, username):
    user = get_object_or_404(User, username=username)

    if request.user.is_authenticated and request.user == user:
        projects = Project.objects.filter(Q(published=True) | Q(created_by=user)).order_by('-created_at')
    else:
        projects = Project.objects.filter(created_by=user, published=True).order_by('-created_at')

    context = {'projects': projects, 'user': user}
    return render(request, 'core/portfolio.html', context)


# --- Project Management ---

@login_required
def create_project(request, username):
    user = get_object_or_404(User, username=username)

    if request.user != user:
        messages.error(request, "You are not authorized to create projects for this user.")
        return redirect('home')

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            messages.success(request, "Project created successfully!")
            return redirect('portfolio', username=user.username)
    else:
        form = ProjectForm()

    context = {'form': form, 'user': user}
    return render(request, 'core/create_project.html', context)


@login_required
def edit_project(request, username, pk):
    user = get_object_or_404(User, username=username)
    project = get_object_or_404(Project, pk=pk, created_by=user)

    if request.user != user:
        messages.error(request, "You are not authorized to edit this project.")
        return redirect('portfolio', username=username)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project updated successfully!")
            return redirect('portfolio', username=username)
    else:
        form = ProjectForm(instance=project)

    context = {'form': form, 'user': user, 'project': project}
    return render(request, 'core/edit_project.html', context)


@login_required
def delete_project(request, username, pk):
    user = get_object_or_404(User, username=username)
    project = get_object_or_404(Project, pk=pk, created_by=user)

    if request.user != user:
        messages.error(request, "You are not authorized to delete this project.")
        return redirect('portfolio', username=username)

    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project deleted successfully!")
        return redirect('portfolio', username=username)

    context = {'project': project, 'user': user}
    return render(request, 'core/confirm_project_delete.html', context)


@login_required
def toggle_project_publish(request, username, pk):
    user = get_object_or_404(User, username=username)
    project = get_object_or_404(Project, pk=pk, created_by=user)

    if request.user != user:
        messages.error(request, "You are not authorized to change publish status.")
        return redirect('portfolio', username=username)

    project.published = not project.published
    project.save()
    messages.success(request, "Project status updated successfully!")
    return redirect('portfolio', username=username)


# --- Profile Management ---

@login_required
def edit_profile(request, username):
    user = get_object_or_404(User, username=username)

    if request.user != user:
        messages.error(request, "You are not authorized to edit this profile.")
        return redirect('home')

    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        # Save first name, last name, email also manually
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        if form.is_valid():
            form.save()
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            messages.success(request, "Profile updated successfully!")
            return redirect('user_profile', username=user.username)
    else:
        form = ProfileForm(instance=profile)

    context = {'form': form, 'user': user}
    return render(request, 'core/edit_profile.html', context)

