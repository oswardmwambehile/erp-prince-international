from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Expense
from .forms import ExpenseForm, ExpenseCategoryForm

import uuid


@login_required
def create_expense(request):

    # =====================================
    # USER COMPANY
    # =====================================
    company = request.user.company

    # =====================================
    # DEFAULT FORMS
    # =====================================
    expense_form = ExpenseForm(
        company=company
    )

    category_form = ExpenseCategoryForm()

    # =====================================
    # HANDLE POST
    # =====================================
    if request.method == 'POST':

        # =================================
        # SAVE CATEGORY
        # =================================
        if 'save_category' in request.POST:

            category_form = ExpenseCategoryForm(
                request.POST
            )

            if category_form.is_valid():

                category_form.save()

                messages.success(
                    request,
                    'Expense category added successfully.'
                )

                return redirect(
                    'create_expense'
                )

            # KEEP EXPENSE FORM
            expense_form = ExpenseForm(
                company=company
            )

        # =================================
        # SAVE EXPENSE
        # =================================
        else:

            expense_form = ExpenseForm(
                request.POST,
                request.FILES,
                company=company
            )

            if expense_form.is_valid():

                expense = expense_form.save(
                    commit=False
                )

                # AUTO COMPANY
                expense.company = company

                # AUTO USER
                expense.submitted_by = request.user

                # AUTO EXPENSE NUMBER
                expense.expense_number = (
                    f"EXP-{uuid.uuid4().hex[:8].upper()}"
                )

                # STATUS = DRAFT DEFAULT
                expense.save()

                messages.success(
                    request,
                    'Expense created successfully.'
                )

                return redirect(
                    'create_expense'
                )

            # KEEP CATEGORY FORM
            category_form = ExpenseCategoryForm()

    context = {

        'expense_form': expense_form,

        'category_form': category_form,

    }

    return render(
        request,
        'manager/create_expense.html',
        context
    )
@login_required
def account_create_expense(request):

    # =====================================
    # USER COMPANY
    # =====================================
    company = request.user.company

    # =====================================
    # DEFAULT FORMS
    # =====================================
    expense_form = ExpenseForm(
        company=company
    )

    category_form = ExpenseCategoryForm()

    # =====================================
    # HANDLE POST
    # =====================================
    if request.method == 'POST':

        # =================================
        # SAVE CATEGORY
        # =================================
        if 'save_category' in request.POST:

            category_form = ExpenseCategoryForm(
                request.POST
            )

            if category_form.is_valid():

                category_form.save()

                messages.success(
                    request,
                    'Expense category added successfully.'
                )

                return redirect('account_create_expense')

            else:
                print(category_form.errors)
                return redirect(
                    'account_create_expense'
                )

            # KEEP EXPENSE FORM
            expense_form = ExpenseForm(
                company=company
            )

        # =================================
        # SAVE EXPENSE
        # =================================
        else:

            expense_form = ExpenseForm(
                request.POST,
                request.FILES,
                company=company
            )

            if expense_form.is_valid():

                expense = expense_form.save(
                    commit=False
                )

                # AUTO COMPANY
                expense.company = company

                # AUTO USER
                expense.submitted_by = request.user

                # AUTO EXPENSE NUMBER
                expense.expense_number = (
                    f"EXP-{uuid.uuid4().hex[:8].upper()}"
                )

                # STATUS = DRAFT DEFAULT
                expense.save()

                messages.success(
                    request,
                    'Expense created successfully.'
                )

                return redirect(
                    'account_expense_list'
                )

            # KEEP CATEGORY FORM
            category_form = ExpenseCategoryForm()

    context = {

        'expense_form': expense_form,

        'category_form': category_form,

    }

    return render(
        request,
        'accounting/create_expense.html',
        context
    )


from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404



from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404


from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ExpenseForm, ExpenseCategoryForm
from .models import Expense


@login_required(login_url='login')
def account_update_expense(request, pk):

    # =====================================
    # USER COMPANY
    # =====================================
    company = request.user.company

    # =====================================
    # GET EXPENSE
    # =====================================
    expense = get_object_or_404(
        Expense,
        pk=pk,
        company=company
    )

    # =====================================
    # DEFAULT FORMS
    # =====================================
    expense_form = ExpenseForm(
        instance=expense,
        company=company
    )

    # User should enter ONLY today's payment
    expense_form.fields["paid_amount"].initial = 0

    category_form = ExpenseCategoryForm(
        company=company
    )

    # =====================================
    # HANDLE POST
    # =====================================
    if request.method == "POST":

        # =================================
        # SAVE CATEGORY
        # =================================
        if "save_category" in request.POST:

            category_form = ExpenseCategoryForm(
                request.POST,
                company=company
            )

            if category_form.is_valid():

                category = category_form.save(
                    commit=False
                )

                category.company = company
                category.save()

                messages.success(
                    request,
                    "Expense category added successfully."
                )

                return redirect(
                    "account_update_expense",
                    pk=expense.pk
                )

            expense_form = ExpenseForm(
                instance=expense,
                company=company
            )

            expense_form.fields["paid_amount"].initial = 0

        # =================================
        # UPDATE EXPENSE
        # =================================
        else:

            expense_form = ExpenseForm(
                request.POST,
                request.FILES,
                instance=expense,
                company=company
            )

            if expense_form.is_valid():

                updated_expense = expense_form.save(
                    commit=False
                )

                # Preserve values
                updated_expense.company = company
                updated_expense.submitted_by = (
                    expense.submitted_by
                )
                updated_expense.expense_number = (
                    expense.expense_number
                )

                category_name = ""

                if updated_expense.category:
                    category_name = (
                        updated_expense.category.name
                        .strip()
                        .lower()
                    )

                # =============================
                # ADVANCE SALARY
                # =============================
                if category_name == "advance salary":

                    today_payment = (
                        expense_form.cleaned_data.get(
                            "paid_amount"
                        )
                        or Decimal("0")
                    )

                    previous_paid = (
                        expense.paid_amount
                        or Decimal("0")
                    )

                    total_amount = (
                        updated_expense.amount
                        or Decimal("0")
                    )

                    total_paid = (
                        previous_paid +
                        today_payment
                    )

                    if total_paid > total_amount:
                        total_paid = total_amount

                    updated_expense.paid_amount = (
                        total_paid
                    )

                    updated_expense.remaining_balance = (
                        total_amount -
                        total_paid
                    )

                # =============================
                # COMMISSION
                # =============================
                elif category_name == "commission":

                    updated_expense.paid_amount = (
                        expense.paid_amount
                        or Decimal("0")
                    )

                    updated_expense.remaining_balance = (
                        Decimal("0")
                    )

                # =============================
                # OTHER CATEGORIES
                # =============================
                else:

                    updated_expense.paid_amount = (
                        Decimal("0")
                    )

                    updated_expense.remaining_balance = (
                        Decimal("0")
                    )

                updated_expense.save()

                messages.success(
                    request,
                    "Expense updated successfully."
                )

                return redirect(
                    "account_expense_list"
                )

            category_form = ExpenseCategoryForm(
                company=company
            )

    context = {
        "expense_form": expense_form,
        "category_form": category_form,
        "expense": expense,
        "is_update": True,
    }

    return render(
        request,
        "accounting/create_expense.html",
        context
    )







from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Expense


# =========================================
# EXPENSE LIST
# =========================================
@login_required
def expense_list(request):

    company = request.user.company

    expenses = Expense.objects.filter(
        company=company
    ).select_related(
        'category',
        'submitted_by'
    ).order_by(
        '-created_at'
    )

    context = {
        'expenses': expenses
    }

    return render(
        request,
        'manager/expense_list.html',
        context
    )
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Expense


from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.templatetags.static import static
from django.conf import settings

@login_required
def account_expense_list(request):

    company = request.user.company

    expenses_list = Expense.objects.filter(company=company).select_related(
        'category',
        'submitted_by'
    )
    logo_url = request.build_absolute_uri(static("img/logo.png"))

    # =========================
    # FILTER LOGIC (FIXED)
    # =========================
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    single_date = request.GET.get("date")

    if single_date:
        expenses_list = expenses_list.filter(expense_date=single_date)

    if start_date and end_date:
        expenses_list = expenses_list.filter(expense_date__range=[start_date, end_date])

    elif start_date:
        expenses_list = expenses_list.filter(expense_date__gte=start_date)

    elif end_date:
        expenses_list = expenses_list.filter(expense_date__lte=end_date)

    expenses_list = expenses_list.order_by('-created_at')

    # =========================
    # PAGINATION
    # =========================
    paginator = Paginator(expenses_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'accounting/expense_list.html', {
        'expenses': page_obj,
        'page_obj': page_obj,
         'logo_url': logo_url,
    })
# =========================================
# EXPENSE DETAIL
# =========================================
@login_required
def expense_detail(request, id):

    company = request.user.company

    expense = get_object_or_404(
        Expense,
        id=id,
        company=company
    )

    context = {
        'expense': expense
    }

    return render(
        request,
        'manager/expense_detail.html',
        context
    )
@login_required
def account_expense_detail(request, id):

    company = request.user.company

    expense = get_object_or_404(
        Expense,
        id=id,
        company=company
    )

    context = {
        'expense': expense
    }

    return render(
        request,
        'accounting/expense_detail.html',
        context
    )


# =========================================
# DELETE EXPENSE
# =========================================
@login_required
def delete_expense(request, id):

    company = request.user.company

    expense = get_object_or_404(
        Expense,
        id=id,
        company=company
    )

    if request.method == 'POST':

        expense.delete()

        messages.success(
            request,
            'Expense deleted successfully.'
        )

    return redirect(
        'expense_list'
    )





from django.shortcuts import get_object_or_404, redirect
from .models import Expense

def update_expense_status(request):
    if request.method == "POST":

        expense_id = request.POST.get("expense_id")
        status = request.POST.get("status")

        expense = get_object_or_404(Expense, id=expense_id)
        expense.status = status
        expense.save()

        return redirect("expense_list")  
    

from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta

from expenses.models import Expense


@login_required(login_url='login')
def account_dashboard(request):

    company = request.user.company
    today = timezone.now().date()

    week_start = today - timedelta(days=today.weekday())

    # ALL expenses in company (NOT user-based)

    daily_expense = Expense.objects.filter(
        company=company,
        expense_date=today
    ).aggregate(total=Sum('amount'))['total'] or 0

    weekly_expense = Expense.objects.filter(
        company=company,
        expense_date__gte=week_start,
        expense_date__lte=today
    ).aggregate(total=Sum('amount'))['total'] or 0

    monthly_expense = Expense.objects.filter(
        company=company,
        expense_date__year=today.year,
        expense_date__month=today.month
    ).aggregate(total=Sum('amount'))['total'] or 0

    yearly_expense = Expense.objects.filter(
        company=company,
        expense_date__year=today.year
    ).aggregate(total=Sum('amount'))['total'] or 0

    # Optional: total expenses count
    total_expenses = Expense.objects.filter(company=company).count()

    return render(request, 'accounting/home_account.html', {
        'daily_expense': daily_expense,
        'weekly_expense': weekly_expense,
        'monthly_expense': monthly_expense,
        'yearly_expense': yearly_expense,
        'total_expenses': total_expenses,
    })

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from xhtml2pdf import pisa
from io import BytesIO

from django.db.models import Sum

from .models import Expense


from decimal import Decimal
from datetime import datetime
from io import BytesIO

from django.contrib.auth.decorators import login_required
from django.templatetags.static import static
from django.db.models import Sum
from django.http import HttpResponse
from django.template.loader import render_to_string

from xhtml2pdf import pisa

from .models import Expense, DailyCashBalance


@login_required(login_url="login")
def expense_report_pdf(request):

    company = request.user.company

    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    single_date = request.GET.get("date")

    logo_url = request.build_absolute_uri(
        static("img/logo.png")
    )

    expenses = Expense.objects.filter(
        company=company
    )

    # ================= FILTER =================

    if single_date:
        report_date = datetime.strptime(
            single_date,
            "%Y-%m-%d"
        ).date()

        expenses = expenses.filter(
            expense_date=report_date
        )

    elif start_date and end_date:
        start = datetime.strptime(
            start_date,
            "%Y-%m-%d"
        ).date()

        end = datetime.strptime(
            end_date,
            "%Y-%m-%d"
        ).date()

        expenses = expenses.filter(
            expense_date__range=[start, end]
        )

    # ================= TOTAL EXPENSE =================

    total = (
        expenses.aggregate(
            total=Sum("amount")
        )["total"]
        or Decimal("0.00")
    )

    # ================= OPENING BALANCE =================

    opening_balance = Decimal("0.00")

    if single_date:

        report_date = datetime.strptime(
            single_date,
            "%Y-%m-%d"
        ).date()

        daily_balance = DailyCashBalance.objects.filter(
            company=company,
            date=report_date
        ).first()

        if daily_balance:
            opening_balance = daily_balance.opening_balance

    elif start_date:

        report_date = datetime.strptime(
            start_date,
            "%Y-%m-%d"
        ).date()

        daily_balance = DailyCashBalance.objects.filter(
            company=company,
            date=report_date
        ).first()

        if daily_balance:
            opening_balance = daily_balance.opening_balance

    # ================= CLOSING BALANCE =================

    closing_balance = opening_balance - total

    # ================= DEBUG =================
    print("--------------------------------")
    print("Company:", company)
    print("Company ID:", company.id)
    print("Single Date:", single_date)
    print("Opening Balance:", opening_balance)
    print("Total Expense:", total)
    print("Closing Balance:", closing_balance)
    print("--------------------------------")

    # ================= CONTEXT =================

    context = {
        "company": company,
        "expenses": expenses,
        "total": total,
        "opening_balance": opening_balance,
        "closing_balance": closing_balance,
        "start_date": start_date,
        "end_date": end_date,
        "single_date": single_date,
        "logo_url": logo_url,
    }

    html_string = render_to_string(
        "accounting/expense_report.html",
        context,
        request=request,
    )

    result = BytesIO()

    pdf = pisa.pisaDocument(
        BytesIO(html_string.encode("UTF-8")),
        result,
    )

    if pdf.err:
        return HttpResponse(
            "Error generating PDF",
            status=500,
        )

    response = HttpResponse(
        result.getvalue(),
        content_type="application/pdf",
    )

    response["Content-Disposition"] = (
        'attachment; filename="expense_report.pdf"'
    )

    return response



from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Expense


# =========================================
# COMMISSION EXPENSE LIST
# =========================================
@login_required
def commission_expense_list(request):

    company = request.user.company

    expenses = (
        Expense.objects.filter(
            company=company,
            category__name__iexact='Commision'  # Change to 'Commisions' if that's your category name
        )
        .select_related(
            'category',
            'submitted_by',
            'branch'
        )
        .order_by(
            '-created_at'
        )
    )

    context = {
        'expenses': expenses
    }

    return render(
        request,
        'accounting/expense_list.html',
        context
    )


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Expense


# =========================================
# ADVANCE SALARY EXPENSE LIST
# =========================================
@login_required
def advance_salary_expense_list(request):

    company = request.user.company

    expenses = (
        Expense.objects.filter(
            company=company,
            category__name__iexact='Advance Salary'
        )
        .select_related(
            'category',
            'submitted_by',
            'branch'
        )
        .order_by(
            '-created_at'
        )
    )

    context = {
        'expenses': expenses
    }

    return render(
        request,
        'accounting/advance_expenses_list.html',
        context
    )


from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.models import Company
from .forms import DailyCashBalanceForm
from .models import DailyCashBalance


def create_daily_cash_balance(request):
    prince = Company.objects.get(name="Prince International")

    if request.method == "POST":
        form = DailyCashBalanceForm(request.POST)

        if form.is_valid():

            company = form.cleaned_data["company"]
            date = form.cleaned_data["date"]

            # Check if opening balance already exists
            if DailyCashBalance.objects.filter(
                company=company,
                date=date
            ).exists():

                messages.error(
                    request,
                    f"An opening balance for {date} already exists."
                )

            else:
                cash = form.save(commit=False)

                # If you always want Prince International,
                # uncomment the next line
                # cash.company = prince

                cash.save()

                messages.success(
                    request,
                    "Opening balance created successfully."
                )

                return redirect("create_daily_cash_balance")

    else:
        form = DailyCashBalanceForm(
            initial={
                "company": prince
            }
        )

    return render(
        request,
        "accounting/create_daily_cash_balance.html",
        {
            "form": form
        }
    )


from django.shortcuts import render
from django.core.paginator import Paginator
from django.utils import timezone
from .models import DailyCashBalance


def daily_cash_balance_list(request):

    balances = DailyCashBalance.objects.all().order_by("-date")

    paginator = Paginator(balances, 10)  # 10 records per page

    page_number = request.GET.get("page")

    balances = paginator.get_page(page_number)

    today = timezone.localdate()

    today_balance = DailyCashBalance.objects.filter(
        date=today
    ).first()

    context = {
        "balances": balances,
        "today_balance": today_balance,
    }

    return render(
        request,
        "accounting/daily_cash_balance_list.html",
        context,
    )


from django.shortcuts import get_object_or_404, redirect, render
from .forms import DailyCashBalanceForm
from .models import DailyCashBalance


def update_daily_cash_balance(request, pk):
    balance = get_object_or_404(
        DailyCashBalance,
        pk=pk
    )

    if request.method == "POST":
        form = DailyCashBalanceForm(
            request.POST,
            instance=balance
        )

        if form.is_valid():
            form.save()
            return redirect("daily_cash_balance_list")

    else:
        form = DailyCashBalanceForm(
            instance=balance
        )

    return render(
        request,
        "accounting/create_daily_cash_balance.html",  # use the SAME template
        {
            "form": form,
        },
    )