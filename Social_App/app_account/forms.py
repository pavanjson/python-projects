from django import forms
from app_home.models import Friends
class FriendPrivacy(forms.ModelForm):
    
    class Meta:
        model=Friends
        fields=['privacy']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["privacy"].widget.attrs.update(
            {
                "class":"form-control"
            }
        )
