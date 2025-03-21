from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('create/', views.create_post, name='create_post'),
    path('<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),
]
