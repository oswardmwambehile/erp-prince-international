from django.urls import path
from . import views

urlpatterns = [

    path(
        "employees/",
        views.employee_list,
        name="employee_list",
    ),

    path(
        "employees/create/",
        views.create_employee,
        name="create_employee",
    ),
    path(
    "employees/<int:pk>/",
    views.employee_detail,
    name="employee_detail"
),

path(
    "employees/edit/<int:pk>/",
    views.edit_employee,
    name="edit_employee"
),

   

    # Create Payroll
    path(
        "create/",
        views.create_payroll,
        name="create_payroll"
    ),

    

    # Edit Payroll
    path(
        "<int:pk>/edit/",
        views.edit_payroll,
        name="edit_payroll"
    ),

     path(
        "payroll/",
        views.payroll_list,
        name="payroll_list"
    ),
     path(
        "employee-salary/<int:employee_id>/",
        views.employee_salary,
        name="employee_salary"
    ),

    path(
    "payroll/<int:pk>/",
    views.payroll_detail,
    name="payroll_detail"
),

path(
        "payroll/<int:pk>/process/",
        views.process_payroll,
        name="process_payroll"
    ),

    path(
        "payroll/<int:pk>/pay/",
        views.pay_payroll,
        name="pay_payroll"
    ),

    path(
    "payroll/<int:pk>/export/",
    views.export_payroll_slip,
    name="export_payroll_slip"
),

    
]