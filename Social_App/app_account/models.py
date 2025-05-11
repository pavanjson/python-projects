from django.db import models
import uuid
from app_users.models import Profile

class CBS(models.Model):
    uid = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class NoticeCategory(CBS):
    name=models.CharField(max_length=50)
    yes_active=models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name}"

class Notification(CBS):
    notice_for=models.ForeignKey( Profile, on_delete=models.CASCADE, related_name="notifications")
    title=models.CharField(max_length=150)
    link=models.URLField(max_length=500, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)

    category = models.ForeignKey(NoticeCategory,on_delete=models.CASCADE, related_name="notice")

    def __str__(self) -> str:
        return f"{self.title}"

