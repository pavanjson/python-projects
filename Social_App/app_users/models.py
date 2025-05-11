from typing import Iterable, Optional
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver

class CommonBaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    uid = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def _str_(self):
        return self.email
    

GENDER = [
    ('male', 'Male'),
    ('female', 'Female'),
]
RELATIONS=[
    ('single','Single'),
    ('married','Married'),
    ('in_a_relation','In a relation'),
]

class Profile(CommonBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER)
    birthday = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, default="default.png")
    bio = models.CharField(max_length=300, null=True,blank=True)
    cover_photo = models.ImageField(upload_to="cover_pic/",null=True, blank=True,default="cover.png")
    fill_up = models.BooleanField(default=False)
    registered = models.BooleanField(default=False)
    
    profession = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    status=models.CharField(max_length=20, choices=RELATIONS, default="single")

    def save(self, *args, **kwargs):
        if not self.profile_picture:
            self.profile_picture = "default.png"
        if not self.cover_photo:
            self.cover_photo = "cover.png"

        return super().save(*args, **kwargs)

    def is_fully_filled(self):
        fields_names = [f.name for f in self._meta.get_fields()]
        for field_name in fields_names:
            value = getattr(self, field_name) 
            if value is None or value=='':
                return False
        
        return True
    
    def __str__(self): 
        return f"{self.first_name}"
    
@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs): 
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs): 
    instance.profile.save()

