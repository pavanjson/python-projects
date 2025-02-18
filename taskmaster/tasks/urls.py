# tasks/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),  # Add this line if it's not already there
    path('', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # This should point to your custom login view
]
