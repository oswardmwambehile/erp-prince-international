from django.urls import path

from . import views





urlpatterns = [

    # =====================================
    # CREATE EXPENSE
    # =====================================
    path(
        'create/',
        views.create_expense,
        name='create_expense'
    ),
    path(
        'account_create/',
        views.account_create_expense,
        name='account_create_expense'
    ),

    # =====================================
    # EXPENSE LIST
    # =====================================
    path(
        'list/',
        views.expense_list,
        name='expense_list'
    ),
    path(
        'accounting_list/',
        views.account_expense_list,
        name='account_expense_list'
    ),

    # =====================================
    # EXPENSE DETAIL
    # =====================================
    path(
        'detail/<int:id>/',
        views.expense_detail,
        name='expense_detail'
    ),
    path(
        'accout_detail/<int:id>/',
        views.account_expense_detail,
        name='account_expense_detail'
    ),
   
    # =====================================
    # DELETE EXPENSE
    # =====================================
    path(
        'delete/<int:id>/',
        views.delete_expense,
        name='delete_expense'
    ),
path(
    'update-status/',
    views.update_expense_status,
    name='update_expense_status'
),
path('expenses/report/pdf/', views.expense_report_pdf, name='expense_report_pdf'),

path(
    'accountant_dashboard/',
    views.account_dashboard,
    name='accountant_dashboard'
),
]