from django.contrib.auth.models import User
from django.db import models
from datetime import timedelta

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 👈 MUST be user
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    duration = models.DurationField()
    location = models.CharField(max_length=255)

    @property
    def end_time(self):
        return self.date + self.duration



class RSVP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='yes')  # ✅ Ensure this is here
    responded_at = models.DateTimeField(auto_now_add=True)


