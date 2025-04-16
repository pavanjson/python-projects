from django import forms
from .models import Subscriber, Newsletter, Group, User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SubscriberForm(forms.ModelForm):
    new_group = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Or create a new group'})
    )

    class Meta:
        model = Subscriber
        fields = ['email', 'group']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].required = False  # ✅ Make it optional

    def clean(self):
        cleaned_data = super().clean()
        group = cleaned_data.get('group')
        new_group = cleaned_data.get('new_group')

        if not group and not new_group:
            raise forms.ValidationError("Please select a group or enter a new group name.")

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['subject', 'content', 'group']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
        }
