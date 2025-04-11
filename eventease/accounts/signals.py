from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # ✅ create profile if not exists (even during login)
    Profile.objects.get_or_create(user=instance, defaults={'name': instance.username})
