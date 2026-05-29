from django.urls import path
from . import views

app_name = "quotations"

urlpatterns = [
    path("create/", views.create_quotation, name="create_quotation"),
    path("sales_create/", views.sales_create_quotation, name="sales_create_quotation"),
    path("<int:pk>/", views.quotation_detail, name="quotation_detail"),
    path("sales_quotation/<int:pk>/", views.sales_quotation_detail, name="sales_quotation_detail"),
     # LIST
    path(
        'quotation_list/',
        views.quotation_list,
        name='quotation_list'
    ),
    path(
        'sales_quotation_list/',
        views.sales_quotation_list,
        name='sales_quotation_list'
    ),

    path(
    '<int:pk>/edit/',
    views.update_quotation,
    name='update_quotation'
),
    path(
    'sales_update<int:pk>/edit/',
    views.sales_update_quotation,
    name='sales_update_quotation'
),

path(
    "quotation/<int:pk>/delete/",
    views.delete_quotation,
    name="delete_quotation"
),
path('quotation/<int:pk>/pdf/', views.quotation_pdf, name='quotation_pdf'),
]