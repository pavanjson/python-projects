from django import forms
from .models import GroupMessage

class GroupMessageForm(forms.ModelForm):    
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets={
            'body': forms.Textarea(attrs={
                "placeholder":"Type your message",
                "class":"form-control mb-sm-0 mb-3",
                "rows":"1",
                "data-autoresize":"",
                })
        }
