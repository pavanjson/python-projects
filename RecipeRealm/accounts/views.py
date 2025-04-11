from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect after successful login
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'accounts/login.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validation
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif password1 != password2:
            messages.error(request, "Passwords do not match.")
        else:
            # Create user
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, "Account created successfully! You can now login.")
            return redirect('login')

    return render(request, 'accounts/register.html')


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')  # Redirect after logout

    return render(request, 'accounts/logout.html')
