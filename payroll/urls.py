from django.urls import path
from . import views

urlpatterns = [

    path(
        "employees/",
        views.employee_list,
        name="employee_list",
    ),

    path(
        "manager_employees/",
        views.admin_employee_list,
        name="admin_employee_list",
    ),
path(
        "employees/create/",
        views.create_employee,
        name="create_employee",
    ),
    


    path(
        "manager_employees/create/",
        views.admin_create_employee,
        name="admin_create_employee",
    ),
    path(
    "employees/<int:pk>/",
    views.employee_detail,
    name="employee_detail"
),

path(
    "admin_edit_employees_/<int:pk>/",
    views.admin_employee_detail,
    name="admin_employee_detail"
),

path(
    "employees/edit/<int:pk>/",
    views.edit_employee,
    name="edit_employee"
),

path(
    "admin-edit-employees/edit/<int:pk>/",
    views.admin_edit_employee,
    name="admin_edit_employee"
),


   

    # Create Payroll
    path(
        "create/",
        views.create_payroll,
        name="create_payroll"
    ),

    # Create Payroll
    path(
        "admin_create/",
        views.admin_create_payroll,
        name="admin_create_payroll"
    ),


    

    # Edit Payroll
    path(
        "<int:pk>/edit/",
        views.edit_payroll,
        name="edit_payroll"
    ),

    # Edit Payroll
    path(
        "admin-edit-payroll<int:pk>/edit/",
        views.admin_edit_payroll,
        name="admin_edit_payroll"
    ),

     path(
        "payroll/",
        views.payroll_list,
        name="payroll_list"
    ),
    
      path(
        "admin_payroll/",
        views.admin_payroll_list,
        name="admin_payroll_list"
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
    "admin_payroll/<int:pk>/",
    views.admin_payroll_detail,
    name="admin_payroll_detail"
),

path(
        "payroll/<int:pk>/process/",
        views.process_payroll,
        name="process_payroll"
    ),

    path(
        "admin_payroll/<int:pk>/process/",
        views.admin_process_payroll,
        name="admin_process_payroll"
    ),


    path(
        "payroll/<int:pk>/pay/",
        views.pay_payroll,
        name="pay_payroll"
    ),

path(
        "admin_pay_payroll/<int:pk>/pay/",
        views.admin_pay_payroll,
        name="admin_pay_payroll"
    ),
    path(
    "payroll/<int:pk>/export/",
    views.export_payroll_slip,
    name="export_payroll_slip"
),

    
]