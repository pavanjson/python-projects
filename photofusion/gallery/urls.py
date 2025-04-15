from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_photo, name='upload'),
    path('edit/<int:photo_id>/', views.edit_photo, name='edit_photo'),
    path('delete/<int:photo_id>/', views.delete_photo, name='delete_photo'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('delete-account/', views.delete_account, name='delete_account'),
]
