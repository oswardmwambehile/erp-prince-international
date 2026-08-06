from django.urls import path
from . import views

urlpatterns = [
    path(
        "create/",
        views.quotation_create,
        name="quotation_create",
    ),
    path(
        "normal-quotations/",
        views.normal_quotation_list,
        name="normal_quotation_list"
    ),

    path(
    "normal_quotations/<int:pk>/",
    views.normal_quotation_detail,
    name="normal-quotation_detail"

),

path(
    "quotations/<int:pk>/pdf/",
    views.quotation_pdf,
    name="normal-quotation_pdf"
),

    
]