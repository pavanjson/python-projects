from django import forms
from .models import Book, Transaction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'publication_date', 'num_available']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }

class TransactionForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
         model = Transaction
         fields = ['due_date']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
         model = User
         fields = ('username', 'email', 'password1', 'password2')
