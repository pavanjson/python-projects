from django import forms
from .models import Comment, Post, Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

BANNED_WORDS = ['spam', 'viagra', 'buy now']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    def clean_text(self):
        text = self.cleaned_data.get('text')
        for banned_word in BANNED_WORDS:
            if banned_word in text.lower():
                raise forms.ValidationError("Your comment contains banned words.")
        return text

class PostForm(forms.ModelForm):
    # Accept comma-separated tags
    tags = forms.CharField(required=False, help_text="Enter tags separated by commas.")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
