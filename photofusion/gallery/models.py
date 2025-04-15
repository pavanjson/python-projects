from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Album(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
