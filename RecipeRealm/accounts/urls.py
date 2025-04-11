from django.urls import path
from django.contrib.auth import views as auth_views
from .views import user_login, user_logout, register

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),

    # Django built-in authentication views (Optional)
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="password_reset"),
    # path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_done"),
    # path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name="password_reset_confirm"),
    # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name="password_reset_complete"),
]
