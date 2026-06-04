from django.urls import path
from .import views

urlpatterns = [
    path('journal/create/', views.create_journal_entry_view, name='create_journal_entry'),
    path("account-types/", views.account_type_list_create, name="account_type_list_create"),
    path("accounts/chart/", views.chart_of_accounts, name="chart_of_accounts"),
    path(
        "journals/",
        views.journal_list,
        name="journal_list"
    ),
    path("general-ledger/", views.general_ledger_view, name="general_ledger"),
     path("trial-balance/", views.trial_balance_view, name="trial_balance"),
     path("income-statement/", views.income_statement_view, name="income_statement"),
    path("balance-sheet/", views.balance_sheet_view, name="balance_sheet"),
]