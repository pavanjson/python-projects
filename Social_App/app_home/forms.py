from django import forms
from .models import PostImage, Posts, FriendRequests, Friends

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields=["content", "privacy"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget.attrs.update(
            {
            "class":"form-control pe-4 border-0",
            "rows":"2",
            "data-autoresize":"",
            "placeholder":"Share your thoughts..."
            }
        )
        self.fields["privacy"].widget.attrs.update(
            {
            "class":"form-select js-choice choice-select-text-none",
            "data-position":"top",            
            }
        )

from .models import Comment

class FriendsForm(forms.ModelForm):
    class Meta:
        model = Friends
        fields = '__all__'

class FriendRequestsForm(forms.ModelForm):
    class Meta:
        model = FriendRequests
        fields = '__all__'

class PostImageForm(forms.ModelForm):
    
    class Meta:
        model = PostImage
        fields = "__all__"
        exclude=['post']
