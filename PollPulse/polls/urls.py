from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_dashboard, name='user_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('polls/', views.poll_list, name='poll_list'),
    path('polls/search/', views.poll_search, name='poll_search'),
    path('polls/create/', views.poll_create, name='poll_create'),
    path('polls/<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('polls/<int:poll_id>/edit/', views.poll_update, name='poll_update'),
    path('polls/<int:poll_id>/delete/', views.poll_delete, name='poll_delete'),
    path('polls/<int:poll_id>/results/', views.poll_results, name='poll_results'),
    path('polls/<int:poll_id>/results/json/', views.poll_results_json, name='poll_results_json'),
]
