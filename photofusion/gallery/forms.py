from django import forms
from django.contrib.auth.models import User
from .models import Photo, Album, Profile

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class PhotoForm(forms.ModelForm):
    album = forms.ModelChoiceField(
        queryset=Album.objects.none(),
        required=False,
        empty_label="Select an album (if available)",
        label="Select Existing Album"
    )
    new_album = forms.CharField(
        required=False,
        max_length=100,
        label="Or Create New Album",
        widget=forms.TextInput(attrs={'placeholder': 'New Album Name'})
    )

    class Meta:
        model = Photo  # ✅ This is crucial
        fields = ['album', 'new_album', 'image', 'caption']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PhotoForm, self).__init__(*args, **kwargs)
        if user:
            albums = Album.objects.filter(user=user)
            self.fields['album'].queryset = albums
            if not albums.exists():
                self.fields['album'].empty_label = "No albums available. Please create one."

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']