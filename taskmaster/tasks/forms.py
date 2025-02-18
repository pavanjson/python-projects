from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'completed', 'due_date', 'repeat']
        widgets = {
            'title': forms.TextInput(attrs={'maxlength': 400, 'style': 'width: 100%;'}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 5, 'style': 'width: 100%;'}),
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))

    password2 = forms.CharField(
        label="Confirm Password",  # Custom label for password2
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Choose a username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Choose a password', 'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email
