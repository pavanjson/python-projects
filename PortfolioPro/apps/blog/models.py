from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Import the built-in User model

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # New field

    def __str__(self):
        return self.title
