# PortfolioPro/apps/core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # User-specific Portfolio Pages
    path('portfolio/<str:username>/', views.user_profile, name='user_profile'),
    path('portfolio/<str:username>/about/', views.about, name='about'),
    path('portfolio/<str:username>/projects/', views.portfolio, name='portfolio'),
    path('portfolio/<str:username>/contact/', views.contact, name='contact'),
    path('portfolio/<str:username>/edit-profile/', views.edit_profile, name='edit_profile'),

    # Project management (create/edit/delete projects) [Admin HRD or owner side maybe]
    path('portfolio/<str:username>/projects/create/', views.create_project, name='create_project'),
    path('portfolio/<str:username>/projects/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('portfolio/<str:username>/projects/<int:pk>/delete/', views.delete_project, name='delete_project'),
    path('portfolio/<str:username>/projects/<int:pk>/toggle/', views.toggle_project_publish, name='toggle_project_publish'),

    # Register Page
    path('register/', views.register, name='register'),
]
