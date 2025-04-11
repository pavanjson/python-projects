from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home/Landing Page
    path('dashboard/', views.dashboard, name='dashboard'),  # User's events
    path('create/', views.create_event, name='create_event'),  # Create event
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),  # Edit event
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),  # View event details
    path('reminders/', views.reminders, name='reminders'),  # Upcoming event reminders
path('event/<int:event_id>/send-invite/', views.send_invitation_email, name='send_invite'),
    ]
