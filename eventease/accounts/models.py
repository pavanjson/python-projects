from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

# 🔁 Auto-create or update profile when a User is created or saved
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Check if a profile exists for this user, and if not, create it
    if created:
        Profile.objects.create(user=instance)
    else:
        # If user is saved and profile exists, update the profile
        instance.profile.save()
