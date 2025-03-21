from django import forms
from .models import Project

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message'}))

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'published']
