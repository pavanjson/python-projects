# django_task_management_system/urls.py

# Import the admin module from django.contrib
from django.contrib import admin
# Import the include and path functions from django.urls
from django.urls import include, path

# Define the URL patterns for this module
urlpatterns = [
    # When the 'admin/' URL is requested, Django will serve the built-in admin site
    path('admin/', admin.site.urls),
    # When the root URL ('') is requested, Django will look for URLs in 'base.urls'
    path('', include('base.urls')),
]