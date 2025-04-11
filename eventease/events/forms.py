from django import forms
from .models import Event, RSVP
from datetime import timedelta

from django import forms
from datetime import timedelta
from .models import Event, RSVP


class EventForm(forms.ModelForm):
    duration = forms.CharField(
        help_text="Format: HH:MM:SS (e.g., 01:30:00 for 1 hour 30 minutes)",
        widget=forms.TextInput(attrs={'placeholder': 'e.g. 01:30:00 for 1hr 30min'})
    )

    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'duration', 'location']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean_duration(self):
        value = self.cleaned_data['duration']
        try:
            # Parse HH:MM:SS string
            hours, minutes, seconds = map(int, value.strip().split(":"))
            return timedelta(hours=hours, minutes=minutes, seconds=seconds)
        except Exception:
            raise forms.ValidationError("Enter duration in HH:MM:SS format (e.g. 01:30:00)")

class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['status']
