from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages

from .models import Employee
from .forms import EmployeeForm

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from .models import Employee


def employee_list(request):
    search = request.GET.get("search", "")

    employees = Employee.objects.select_related(
        "user"
    ).order_by("-id")

    if search:
        employees = employees.filter(
            Q(user__first_name__icontains=search) |
            Q(user__last_name__icontains=search) |
            Q(user__email__icontains=search) |
            Q(employee_id__icontains=search)
        )

    paginator = Paginator(employees, 25)
    page = request.GET.get("page")
    employees = paginator.get_page(page)

    return render(
        request,
        "hr/employee_list.html",
        {
            "employees": employees,
            "search": search,
        },
    )

def create_employee(request):

    if request.method == "POST":

        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Employee created successfully.")
            return redirect("employee_list")

    else:
        form = EmployeeForm()

    return render(
        request,
        "hr/employee_form.html",
        {
            "form": form,
        },
    )


from django.shortcuts import get_object_or_404, render

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    return render(
        request,
        "hr/employee_detail.html",
        {
            "employee": employee
        }
    )


from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

def edit_employee(request, pk):

    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":

        form = EmployeeForm(
            request.POST,
            instance=employee
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Employee updated successfully."
            )

            return redirect("employee_list")

    else:

        form = EmployeeForm(
            instance=employee
        )

    return render(
        request,
        "hr/employee_form.html",
        {
            "form": form,
            "employee": employee,
            "page_title": "Edit Employee",
            "button_text": "Update Employee",
        },
    )


# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse

from .models import Payroll
from .forms import PayrollForm

def generate_payroll_number():


        last_payroll = Payroll.objects.order_by("-id").first()

        if last_payroll:

            try:
                last_number = int(
                    last_payroll.payroll_number.replace("PAY", "")
                )
            except:
                last_number = 0

            next_number = last_number + 1

        else:

            next_number = 1

        return f"PAY{next_number:05d}"
        

def create_payroll(request):

    
        if request.method == "POST":

            form = PayrollForm(request.POST)

            if form.is_valid():

                payroll = form.save(commit=False)

                payroll.company = request.user.company

                payroll.processed_by = request.user

                payroll.payroll_number = generate_payroll_number()

                payroll.basic_salary = payroll.employee.salary

                payroll.save()

                messages.success(
                    request,
                    "Payroll created successfully."
                )

                return redirect("payroll_list")

        else:

            form = PayrollForm()

        return render(
            request,
            "hr/payroll_form.html",
            {
                "form": form,
                "page_title": "Create Payroll",
                "button_text": "Save Payroll",
            },
        )
def employee_salary(request, employee_id):

    try:

        employee = Employee.objects.get(
            pk=employee_id
        )

        return JsonResponse({
            "salary": float(employee.salary)
        })

    except Employee.DoesNotExist:

        return JsonResponse({
            "salary": 0
        })



def edit_payroll(request, pk):


        payroll = get_object_or_404(
            Payroll,
            pk=pk
        )

        if request.method == "POST":

            form = PayrollForm(
                request.POST,
                instance=payroll
            )

            if form.is_valid():

                payroll = form.save(commit=False)

                payroll.basic_salary = payroll.employee.salary

                payroll.save()

                messages.success(
                    request,
                    "Payroll updated successfully."
                )

                return redirect("payroll_list")

        else:

            form = PayrollForm(
                instance=payroll
            )

        return render(
            request,
            "hr/payroll_form.html",
            {
                "form": form,
                "page_title": "Edit Payroll",
                "button_text": "Update Payroll",
                "payroll": payroll,
            },
        )




from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Payroll


def payroll_list(request):

    payrolls = Payroll.objects.select_related(
        "employee",
        "employee__user"
    ).order_by("-id")

    paginator = Paginator(payrolls, 20)

    page_number = request.GET.get("page")

    payrolls = paginator.get_page(page_number)

    return render(
        request,
        "hr/payroll_list.html",
        {
            "payrolls": payrolls
        }
    )


from django.shortcuts import get_object_or_404, render

def payroll_detail(request, pk):

    payroll = get_object_or_404(
        Payroll.objects.select_related(
            "employee",
            "employee__user",
            "processed_by"
        ),
        pk=pk
    )

    return render(
        request,
        "hr/payroll_detail.html",
        {
            "payroll": payroll
        }
    )

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone

from .models import Payroll


def process_payroll(request, pk):

    payroll = get_object_or_404(
        Payroll,
        pk=pk
    )

    if payroll.status == "draft":

        payroll.status = "processed"
        payroll.processed_by = request.user
        payroll.processed_at = timezone.now()

        payroll.save()

        messages.success(
            request,
            f"{payroll.payroll_number} processed successfully."
        )

    else:

        messages.warning(
            request,
            "Only draft payrolls can be processed."
        )

    return redirect("payroll_list")


def pay_payroll(request, pk):

    payroll = get_object_or_404(
        Payroll,
        pk=pk
    )

    if payroll.status == "processed":

        payroll.status = "paid"

        payroll.save()

        messages.success(
            request,
            f"{payroll.payroll_number} marked as paid."
        )

    else:

        messages.warning(
            request,
            "Payroll must be processed before payment."
        )

    return redirect("payroll_list")




from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from .models import Payroll


def export_payroll_slip(request, pk):

    payroll = get_object_or_404(
        Payroll.objects.select_related(
            "employee",
            "employee__user"
        ),
        pk=pk
    )

    response = HttpResponse(
        content_type="application/pdf"
    )

    response[
        "Content-Disposition"
    ] = (
        f'attachment; '
        f'filename="Payslip-{payroll.payroll_number}.pdf"'
    )

    doc = SimpleDocTemplate(response)

    styles = getSampleStyleSheet()

    elements = []

    # =========================
    # COMPANY HEADER
    # =========================

    elements.append(
        Paragraph(
            "PRINCE INTERNATIONAL LTD",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(
            "EMPLOYEE PAYROLL SLIP",
            styles["Heading2"]
        )
    )

    elements.append(Spacer(1, 20))

    # =========================
    # EMPLOYEE INFORMATION
    # =========================

    employee_data = [

        ["Payroll Number", payroll.payroll_number],

        [
            "Employee",
            f"{payroll.employee.user.first_name} "
            f"{payroll.employee.user.last_name}"
        ],

        [
            "Employee ID",
            payroll.employee.employee_id
        ],

        [
            "Payroll Period",
            f"{payroll.payroll_month}/{payroll.payroll_year}"
        ],

        [
            "Status",
            payroll.get_status_display()
        ],

    ]

    employee_table = Table(
        employee_data,
        colWidths=[180, 300]
    )

    employee_table.setStyle(
        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (0, -1),
                colors.HexColor("#E5E7EB")
            ),

            (
                "FONTNAME",
                (0, 0),
                (-1, -1),
                "Helvetica-Bold"
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.grey
            ),

            (
                "PADDING",
                (0, 0),
                (-1, -1),
                8
            ),

        ])
    )

    elements.append(employee_table)

    elements.append(Spacer(1, 25))

    # =========================
    # SALARY BREAKDOWN TITLE
    # =========================

    elements.append(
        Paragraph(
            "Salary Breakdown",
            styles["Heading3"]
        )
    )

    elements.append(Spacer(1, 10))

    # =========================
    # SALARY TABLE
    # =========================

    salary_data = [

        [
            "Description",
            "Amount (TZS)"
        ],

        [
            "Basic Salary",
            f"{payroll.basic_salary:,.2f}"
        ],

        [
            "Allowance",
            f"{payroll.allowance:,.2f}"
        ],

        [
            "Deduction",
            f"{payroll.deduction:,.2f}"
        ],

        [
            "Tax",
            f"{payroll.tax:,.2f}"
        ],

        [
            "Net Salary",
            f"{payroll.net_salary:,.2f}"
        ],

    ]

    salary_table = Table(
        salary_data,
        colWidths=[250, 230]
    )

    salary_table.setStyle(
        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#166534")
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),

            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.grey
            ),

            (
                "BACKGROUND",
                (0, 1),
                (-1, -2),
                colors.whitesmoke
            ),

            (
                "BACKGROUND",
                (0, -1),
                (-1, -1),
                colors.HexColor("#DCFCE7")
            ),

            (
                "TEXTCOLOR",
                (0, -1),
                (-1, -1),
                colors.HexColor("#166534")
            ),

            (
                "FONTNAME",
                (0, -1),
                (-1, -1),
                "Helvetica-Bold"
            ),

            (
                "ALIGN",
                (1, 1),
                (1, -1),
                "RIGHT"
            ),

            (
                "PADDING",
                (0, 0),
                (-1, -1),
                10
            ),

        ])
    )

    elements.append(salary_table)

    elements.append(Spacer(1, 40))

    # =========================
    # SUMMARY BOX
    # =========================

    summary_data = [
        [
            "NET SALARY PAYABLE",
            f"TZS {payroll.net_salary:,.2f}"
        ]
    ]

    summary_table = Table(
        summary_data,
        colWidths=[250, 230]
    )

    summary_table.setStyle(
        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (-1, -1),
                colors.HexColor("#166534")
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, -1),
                colors.white
            ),

            (
                "FONTNAME",
                (0, 0),
                (-1, -1),
                "Helvetica-Bold"
            ),

            (
                "FONTSIZE",
                (0, 0),
                (-1, -1),
                14
            ),

            (
                "ALIGN",
                (1, 0),
                (1, 0),
                "RIGHT"
            ),

            (
                "PADDING",
                (0, 0),
                (-1, -1),
                12
            ),

        ])
    )

    elements.append(summary_table)

    elements.append(Spacer(1, 60))

    # =========================
    # SIGNATURE SECTION
    # =========================

    signature_table = Table(
        [
            [
                "Prepared By",
                "Approved By",
                "Employee"
            ],
            [
                "",
                "",
                ""
            ]
        ],
        colWidths=[170, 170, 170]
    )

    signature_table.setStyle(
        TableStyle([

            (
                "ALIGN",
                (0, 0),
                (-1, -1),
                "CENTER"
            ),

            (
                "LINEABOVE",
                (0, 1),
                (-1, 1),
                1,
                colors.black
            ),

            (
                "TOPPADDING",
                (0, 1),
                (-1, 1),
                30
            ),

        ])
    )

    elements.append(signature_table)

    doc.build(elements)

    return response