from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name='login'),
    path('admin_dashboard/', views.dashboard, name='dashboard'),
    path('sales_dashboard/', views.sales_dashboard, name='sales_dashboard'),
    
    path('companies/', views.company_view, name='company_view'),
    path(
        'branches/',
        views.branch_view,
        name='branch_view'
    ),
    path(
        'department/',
        views.department_view,
        name='department_view'
    ),
     path(
        'positions/',
        views.position_view,
        name='position_view'
    ),

    path('users/', views.user_view, name='user_view'),
     path('logout/', views.logout_user, name='logout'),

    # =========================
    # USER DETAIL PAGE
    # =========================
    path('users/<int:pk>/', views.user_detail_view, name='user_detail_view'),


]