from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('save/', views.save_favorite, name="save_favorite"),
    path('delete/<str:city>/', views.delete_favorite, name="delete_favorite"),
    path('weather/<str:city>/', views.weather_by_city, name="weather_by_city"),  # New route
]
