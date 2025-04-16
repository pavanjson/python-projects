from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/add/', views.movie_create, name='movie_add'),
    path('movie/<int:pk>/edit/', views.movie_edit, name='movie_edit'),
    path('movie/<int:pk>/delete/', views.movie_delete, name='movie_delete'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('movie/<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('movie/<int:movie_pk>/review/edit/', views.edit_review, name='edit_review'),
    path('movie/<int:movie_pk>/review/delete/', views.delete_review, name='delete_review'),

]
