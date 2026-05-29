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
                    'account_create_expense'
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


@login_required
def account_expense_list(request):

    company = request.user.company

    expenses_list = Expense.objects.filter(
        company=company
    ).select_related(
        'category',
        'submitted_by'
    ).order_by('-created_at')

    # ✅ PAGINATION (10 per page)
    paginator = Paginator(expenses_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'expenses': page_obj,   # IMPORTANT (replace queryset)
        'page_obj': page_obj
    }

    return render(
        request,
        'accounting/expense_list.html',
        context
    )


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
        'eexpense_list'
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

