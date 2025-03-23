from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Workout, Goal


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove default help texts
        self.fields['username'].help_text = ''
        self.fields['email'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['exercise_type', 'duration', 'calories_burned', 'workout_date']
        widgets = {
            'workout_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'exercise_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Exercise Type'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration in minutes'}),
            'calories_burned': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Calories Burned'}),
        }


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['description', 'target_date', 'is_completed']
        widgets = {
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Goal description', 'rows': 3}),
            'target_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
