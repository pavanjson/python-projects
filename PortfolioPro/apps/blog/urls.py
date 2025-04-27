from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('<str:username>/blog/', views.blog_list, name='blog_list'),
    path('<str:username>/blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<str:username>/blog/create/', views.create_post, name='create_post'),
    path('<str:username>/blog/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('<str:username>/blog/<int:pk>/delete/', views.delete_post, name='delete_post'),
]
