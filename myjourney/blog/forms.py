from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    tags = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select,
        required=False,
        label='Tags',
        empty_label="Select a connection"
    )
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class UserUpdateForm(forms.ModelForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(username=self.instance.username).exists():
            raise ValidationError("Email ID already exists, please try another.")
        return email

    class Meta:
        model = User
        fields = ['username', 'email']

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}),
        required=True,
        label="Username"
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        help_text="Required. Enter a valid email address.",
        label="Email"
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        required=True,
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
        required=True,
        label="Confirm Password"
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email ID already exists, please try another.")
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


