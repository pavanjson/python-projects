from django.contrib import admin
from .models import Company, Job, UserProfile, Application

admin.site.register(Company)
admin.site.register(Job)
admin.site.register(UserProfile)
admin.site.register(Application)
