from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegistrationForm  # or your form
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# ✅ Register
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return render(request, 'accounts/register.html', {'form': form})

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
                return render(request, 'accounts/register.html', {'form': form})

            user = form.save()  # 👈 No profile creation here
            messages.success(request, "Registration successful. Please login.")
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

# ✅ Login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"👋 Welcome back, {user.username}!")
            return redirect('dashboard')  # Ensure 'dashboard' URL is defined
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Check if user exists and provide specific error feedback
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "There was an error processing your login.")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


# ✅ Logout
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')

# ✅ Profile
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')
