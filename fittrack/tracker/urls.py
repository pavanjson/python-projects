from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('log-workout/', views.log_workout, name='log_workout'),
    path('update-workout/<int:pk>/', views.update_workout, name='update_workout'),
    path('delete-workout/<int:pk>/', views.delete_workout, name='delete_workout'),
    path('set-goal/', views.set_goal, name='set_goal'),
    path('update-goal/<int:pk>/', views.update_goal, name='update_goal'),
    path('delete-goal/<int:pk>/', views.delete_goal, name='delete_goal'),
    path('progress/', views.progress_report, name='progress_report'),
    path('profile/', views.profile, name='profile'),
    path('export-workouts/', views.export_workouts, name='export_workouts'),
]
