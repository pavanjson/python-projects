# quiz/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quizzes/', views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/create_dynamic/', views.quiz_create_dynamic, name='quiz_create_dynamic'),
    path('quiz/<int:quiz_id>/edit/', views.quiz_edit, name='quiz_edit'),
    path('quiz/<int:quiz_id>/delete/', views.quiz_delete, name='quiz_delete'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
