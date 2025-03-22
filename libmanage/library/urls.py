from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Books
    path('books/', views.book_list, name='book_list'),
    path('books/new/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),

    # Transactions (user-side)
    path('books/<int:book_id>/request/', views.request_rent_book, name='request_rent_book'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/<int:transaction_id>/return-request/', views.request_early_return, name='request_early_return'),

    # Admin management
    path('manage/requests/', views.manage_requests, name='manage_requests'),
    path('manage/requests/<int:transaction_id>/approve/', views.approve_request, name='approve_request'),
    path('manage/requests/<int:transaction_id>/deny/', views.deny_request, name='deny_request'),
    path('manage/requests/<int:transaction_id>/issue/', views.issue_book_admin, name='issue_book_admin'),

    # Returns (admin-side)
    path('manage/returns/', views.manage_return_requests, name='manage_return_requests'),
    path('manage/returns/<int:transaction_id>/update/', views.update_return, name='update_return'),

    # Authentication
    path('register/', views.register, name='register'),
]
