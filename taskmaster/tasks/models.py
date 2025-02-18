from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now, timedelta

class Task(models.Model):
    PRIORITY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )

    REPEAT_CHOICES = (
        ('none', 'No Repeat'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)  # Task deadline
    repeat = models.CharField(max_length=10, choices=REPEAT_CHOICES, default='none')  # Recurring tasks

    class Meta:
        db_table = 'task_table'

    def __str__(self):
        return f"{self.title} ({self.priority})"
