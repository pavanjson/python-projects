from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.registration, name="signup"),
    path('register-details/',views.registration_step2, name="signup_details"),
    path('login/',views.login_page, name="login_page"),
    path('logout/',views.logout_view, name="logout"),

]
