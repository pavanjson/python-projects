from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('company/<int:company_id>/', views.company_profile, name='company_profile'),
    path('profile/', views.user_profile, name='user_profile'),
    path('signup/', views.signup, name='signup'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('applications/', views.my_applications, name='my_applications'),
]
