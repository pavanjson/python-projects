from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subscribers/', views.manage_subscribers, name='manage_subscribers'),
    path('compose/', views.compose_newsletter, name='compose_newsletter'),
    path('sent/', views.sent_newsletters, name='sent_newsletters'),
    path('groups/', views.group_list, name='group_list'),
    path('groups/delete/<int:group_id>/', views.delete_group, name='delete_group'),
    path('groups/<int:group_id>/', views.group_detail, name='group_detail'),
    path('subscriber/delete/<int:subscriber_id>/', views.delete_subscriber, name='delete_subscriber'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('sent/<int:newsletter_id>/', views.newsletter_detail, name='newsletter_detail'),
]
