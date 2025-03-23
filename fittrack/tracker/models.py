from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_type = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in minutes")
    calories_burned = models.IntegerField()
    workout_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.exercise_type} on {self.workout_date}"

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    target_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - Goal: {self.description}"
