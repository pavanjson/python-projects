from django import forms
from django.contrib.auth.models import User
from .models import Poll, PollOption

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


class PollCreationForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ('question', 'description', 'start_date', 'end_date', 'image')
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }



class PollOptionForm(forms.ModelForm):
    class Meta:
        model = PollOption
        fields = ['option_text']

    def clean_option_text(self):
        option_text = self.cleaned_data.get('option_text')
        if option_text:
            option_text = option_text.strip()  # Trim leading/trailing spaces
        return option_text
