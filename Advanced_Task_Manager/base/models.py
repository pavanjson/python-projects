# base/models.py

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Define choices for task status
TASK_STATUS_CHOICES =  (
    ('todo', 'To Do'),
    ('started', 'Started'),
    ('complete', 'Complete'),
    ('archived', 'Archived'),
)

# Define Task model
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True) # RichTextField is a WYSIWYG editor
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES, default='todo')
    due = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)

    # String representation of the task
    def __str__(self):
        return self.title  # Use the task's title as its string representation

    # Meta data for the Task model
    class Meta:
        ordering = ['-created']  # Order tasks by the 'created' field in descending order