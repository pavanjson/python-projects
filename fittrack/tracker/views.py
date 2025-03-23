import json, csv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .forms import WorkoutForm, GoalForm, RegistrationForm, ProfileForm
from .models import Workout, Goal


def home(request):
    return render(request, 'tracker/home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'tracker/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials. Please try again.")
    return render(request, 'tracker/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def log_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            messages.success(request, "Workout logged successfully!")
            return redirect('progress_report')
    else:
        form = WorkoutForm()
    return render(request, 'tracker/log_workout.html', {'form': form})


@login_required
def update_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            messages.success(request, "Workout updated successfully!")
            return redirect('progress_report')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'tracker/update_workout.html', {'form': form, 'workout': workout})


@login_required
def delete_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    if request.method == 'POST':
        workout.delete()
        messages.success(request, "Workout deleted successfully!")
        return redirect('progress_report')
    return render(request, 'tracker/delete_workout.html', {'workout': workout})


@login_required
def set_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            messages.success(request, "Goal set successfully!")
            return redirect('progress_report')
    else:
        form = GoalForm()
    return render(request, 'tracker/set_goal.html', {'form': form})


@login_required
def update_goal(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            messages.success(request, "Goal updated successfully!")
            return redirect('progress_report')
    else:
        form = GoalForm(instance=goal)
    return render(request, 'tracker/update_goal.html', {'form': form, 'goal': goal})


@login_required
def delete_goal(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    if request.method == 'POST':
        goal.delete()
        messages.success(request, "Goal deleted successfully!")
        return redirect('progress_report')
    return render(request, 'tracker/delete_goal.html', {'goal': goal})


@login_required
def progress_report(request):
    workouts = Workout.objects.filter(user=request.user).order_by('workout_date')
    goals = Goal.objects.filter(user=request.user)

    total_workouts = workouts.count()
    total_duration = sum([w.duration for w in workouts])
    total_calories = sum([w.calories_burned for w in workouts])

    # Prepare data for Chart.js: list of workout dates and calories burned.
    labels = [w.workout_date.strftime("%Y-%m-%d") for w in workouts]
    calories_data = [w.calories_burned for w in workouts]

    context = {
        'workouts': workouts,
        'goals': goals,
        'total_workouts': total_workouts,
        'total_duration': total_duration,
        'total_calories': total_calories,
        'labels': json.dumps(labels),
        'calories_data': json.dumps(calories_data),
    }
    return render(request, 'tracker/progress_report.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'tracker/profile.html', {'form': form})


@login_required
def export_workouts(request):
    workouts = Workout.objects.filter(user=request.user).order_by('workout_date')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="workouts.csv"'
    writer = csv.writer(response)
    writer.writerow(['Workout Date', 'Exercise Type', 'Duration (min)', 'Calories Burned'])
    for w in workouts:
        writer.writerow([w.workout_date, w.exercise_type, w.duration, w.calories_burned])
    return response
