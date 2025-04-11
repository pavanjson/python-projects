from django.urls import path
from . import views
from .views import create_post

urlpatterns = [
    path('', views.home, name='home'),  # ✅ Home URL
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('create/', views.create_post, name='create_post'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.comment_post, name='comment_post'),
    path('follow/<str:username>/', views.follow_user, name='follow_user'),
    path('unfollow/<str:username>/', views.unfollow_user, name='unfollow_user'),
path('create/', create_post, name='create_post'),
path('search/', views.search_users, name='search_users'),
path('delete/<int:post_id>/', views.delete_post, name='delete_post'),

]
