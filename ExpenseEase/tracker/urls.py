from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('expenses/add/', views.add_expense, name='add_expense'),
    path('expenses/edit/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('expenses/delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('budgets/add/', views.add_budget, name='add_budget'),
    path('reports/', views.report, name='report'),
    path('signup/', views.signup, name='signup'),
    path('report/pdf/<str:month>/', views.export_month_pdf, name='export_month_pdf'),
    path('report/excel/<str:month>/', views.export_month_excel, name='export_month_excel'),
]
