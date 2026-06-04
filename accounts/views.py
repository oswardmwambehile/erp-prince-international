from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


def login_user(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=email,
            password=password
        )

        # ❌ ALWAYS HANDLE BOTH CASES PROPERLY

        if user is None:
            messages.error(request, "Invalid email or password")
            return redirect('login')

        if not user.is_active:
            messages.error(request, "Account is inactive")
            return redirect('login')

        login(request, user)

        position = user.position.name if user.position else None

        
        # =========================
        # MANAGER DASHBOARD
        # =========================
        if position == 'Manager':
            return redirect('dashboard')

        # =========================
        # INVENTORY MANAGER
        # =========================
        elif position == 'Inventory Manager':
            return redirect('inventory_dashboard')
        # =========================
        elif position == 'Sales and marketing':
            return redirect('sales_dashboard')
        # =========================
        
        elif position == 'Accountant':
            return redirect('accountant_dashboard')

        # =========================
        # SALES TEAM
        # =========================
        elif position in [
            'Facilitator',
            'Zonal Sales Executive',
            'Corporate Officer',
            'Mobile Sales Officer',
            'Desk Sales Officer'
        ]:
            return redirect('dashboard')

        # =========================
        # DEFAULT
        # =========================
        return redirect('index')

        return redirect('index')

    # ✅ THIS IS IMPORTANT (GET REQUEST)
    return render(request, 'manager/login.html')
from django.shortcuts import render
from django.contrib.auth import get_user_model

from customers.models import Customer
from quotations.models import Quotation
from expenses.models import Expense
from inventory.models import Product, Stock

User = get_user_model()


from django.contrib.auth import get_user_model
from django.db.models import Sum

User = get_user_model()


def dashboard(request):

    # USERS
    total_users = User.objects.count()

    # CUSTOMERS (GLOBAL)
    total_customers = Customer.objects.count()

    # QUOTATIONS (GLOBAL)
    quotations_qs = Quotation.objects.all()

    total_quotations = quotations_qs.count()

    total_quotation_amount = quotations_qs.aggregate(
        total=Sum("grand_total")
    )["total"] or 0

    # EXPENSES (GLOBAL)
    expenses_qs = Expense.objects.all()

    total_expenses = expenses_qs.count()

    total_expense_amount = expenses_qs.aggregate(
        total=Sum("amount")
    )["total"] or 0

    # INVENTORY (GLOBAL)
    total_products = Product.objects.count()
    total_stock = Stock.objects.count()

    context = {
        "total_users": total_users,
        "total_customers": total_customers,

        "total_quotations": total_quotations,
        "total_quotation_amount": total_quotation_amount,

        "total_expenses": total_expenses,
        "total_expense_amount": total_expense_amount,

        "total_products": total_products,
        "total_stock": total_stock,
    }

    return render(request, "manager/homeadmin.html", context)


from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from customers.models import Customer
from inventory.models import Product
from quotations.models import Quotation

@login_required(login_url='login')
def sales_dashboard(request):

    # =====================================
    # TOTAL PRODUCTS
    # =====================================
    total_products = Product.objects.count()

    # =====================================
    # TOTAL CUSTOMERS
    # =====================================
    total_customers = Customer.objects.count()

    # =====================================
    # USER QUOTATIONS ONLY
    # =====================================
    user_quotations = Quotation.objects.filter(
        created_by=request.user
    )

    # =====================================
    # TOTAL USER QUOTATIONS
    # =====================================
    total_quotations = user_quotations.count()

    # =====================================
    # TOTAL SALES AMOUNT
    # =====================================
    total_sales = user_quotations.aggregate(
        total=Sum('grand_total')
    )['total'] or 0

    # =====================================
    # RECENT USER QUOTATIONS
    # =====================================
    recent_quotations = user_quotations.select_related(
        'customer',
        'created_by'
    ).order_by('-created_at')[:5]

    context = {

        'total_products': total_products,

        'total_customers': total_customers,

        'total_quotations': total_quotations,

        'total_sales': total_sales,

        'recent_quotations': recent_quotations,

    }

    return render(
        request,
        'sales/home_sales.html',
        context
    )




from django.shortcuts import render, redirect, get_object_or_404
from .models import Company
from .forms import CompanyForm


def company_view(request):
    form = CompanyForm()

    # CREATE
    if request.method == 'POST' and 'create_company' in request.POST:
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_view')

    # UPDATE
    if request.method == 'POST' and 'update_company' in request.POST:
        company_id = request.POST.get('company_id')
        company = get_object_or_404(Company, id=company_id)
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_view')

    # DELETE
    if request.method == 'POST' and 'delete_company' in request.POST:
        company_id = request.POST.get('company_id')
        company = get_object_or_404(Company, id=company_id)
        company.delete()
        return redirect('company_view')

    companies = Company.objects.all().order_by('-created_at')

    return render(request, 'manager/company.html', {
        'form': form,
        'companies': companies
    })


from django.shortcuts import render, redirect, get_object_or_404
from .models import Branch
from .forms import BranchForm


def branch_view(request):

    form = BranchForm()

    # CREATE
    if request.method == 'POST' and 'create_branch' in request.POST:

        form = BranchForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('branch_view')

    # UPDATE
    if request.method == 'POST' and 'update_branch' in request.POST:

        branch_id = request.POST.get('branch_id')

        branch = get_object_or_404(
            Branch,
            id=branch_id
        )

        form = BranchForm(
            request.POST,
            instance=branch
        )

        if form.is_valid():
            form.save()
            return redirect('branch_view')

    # DELETE
    if request.method == 'POST' and 'delete_branch' in request.POST:

        branch_id = request.POST.get('branch_id')

        branch = get_object_or_404(
            Branch,
            id=branch_id
        )

        branch.delete()

        return redirect('branch_view')

    branches = Branch.objects.select_related(
        'company'
    ).all().order_by('-created_at')

    context = {
        'form': form,
        'branches': branches
    }

    return render(
        request,
        'manager/branch.html',
        context
    )

from django.shortcuts import render, redirect, get_object_or_404
from .models import Department
from .forms import DepartmentForm


def department_view(request):

    form = DepartmentForm()

    # CREATE
    if request.method == 'POST' and 'create_department' in request.POST:

        form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('department_view')

    # UPDATE
    if request.method == 'POST' and 'update_department' in request.POST:

        department_id = request.POST.get('department_id')

        department = get_object_or_404(
            Department,
            id=department_id
        )

        form = DepartmentForm(
            request.POST,
            instance=department
        )

        if form.is_valid():
            form.save()
            return redirect('department_view')

    # DELETE
    if request.method == 'POST' and 'delete_department' in request.POST:

        department_id = request.POST.get('department_id')

        department = get_object_or_404(
            Department,
            id=department_id
        )

        department.delete()

        return redirect('department_view')

    departments = Department.objects.select_related(
        'company'
    ).all().order_by('-created_at')

    context = {
        'form': form,
        'departments': departments
    }

    return render(
        request,
        'manager/department.html',
        context
    )


from django.shortcuts import render, redirect, get_object_or_404
from .models import Position
from .forms import PositionForm


def position_view(request):

    form = PositionForm()

    # CREATE
    if request.method == 'POST' and 'create_position' in request.POST:

        form = PositionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('position_view')

        else:
            print(form.errors)

    # UPDATE
    if request.method == 'POST' and 'update_position' in request.POST:

        position_id = request.POST.get('position_id')

        position = get_object_or_404(
            Position,
            id=position_id
        )

        form = PositionForm(
            request.POST,
            instance=position
        )

        if form.is_valid():
            form.save()
            return redirect('position_view')

        else:
            print(form.errors)

    # DELETE
    if request.method == 'POST' and 'delete_position' in request.POST:

        position_id = request.POST.get('position_id')

        position = get_object_or_404(
            Position,
            id=position_id
        )

        position.delete()

        return redirect('position_view')

    positions = Position.objects.select_related(
        'company'
    ).all().order_by('-created_at')

    context = {
        'form': form,
        'positions': positions
    }

    return render(
        request,
        'manager/position.html',
        context
    )


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import *
from .forms import UserForm


def user_view(request):

    search = request.GET.get('search', '')

    users = User.objects.select_related(
        'company',
        'branch',
        'department',
        'position'
    ).all().order_by('-date_joined')

    # SEARCH
    if search:
        users = users.filter(
            email__icontains=search
        ) | users.filter(
            first_name__icontains=search
        ) | users.filter(
            last_name__icontains=search
        )

    form = UserForm()

    # ==================================================
    # CREATE USER
    # ==================================================
    if request.method == 'POST' and 'create_user' in request.POST:

        form = UserForm(request.POST)

        if form.is_valid():

            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')

            # REQUIRE PASSWORD
            if not password:
                messages.error(
                    request,
                    "Password is required."
                )

                context = {
                    'form': form,
                    'users': users,
                    'search': search,
                    'companies': Company.objects.all(),
                    'branches': Branch.objects.all(),
                    'departments': Department.objects.all(),
                    'positions': Position.objects.all(),
                }

                return render(
                    request,
                    'manager/user.html',
                    context
                )

            # CREATE USER
            user = form.save(commit=False)

            # HASH PASSWORD
            user.set_password(password)

            user.save()

            messages.success(
                request,
                "User created successfully."
            )

            return redirect('user_view')

        else:

            print(form.errors)

            messages.error(
                request,
                form.errors
            )

    # ==================================================
    # UPDATE USER
    # ==================================================
    elif request.method == 'POST' and 'update_user' in request.POST:

        user = get_object_or_404(
            User,
            id=request.POST.get('user_id')
        )

        # IMPORTANT:
        # REMOVE PASSWORD FIELDS FROM POST
        data = request.POST.copy()

        data.pop('password', None)
        data.pop('confirm_password', None)

        form = UserForm(
            data,
            instance=user
        )

        if form.is_valid():

            updated_user = form.save(commit=False)

            # KEEP OLD PASSWORD
            updated_user.password = user.password

            updated_user.save()

            messages.success(
                request,
                "User updated successfully."
            )

            return redirect('user_view')

        else:

            print(form.errors)

            messages.error(
                request,
                form.errors
            )

    # ==================================================
    # DELETE USER
    # ==================================================
    elif request.method == 'POST' and 'delete_user' in request.POST:

        user = get_object_or_404(
            User,
            id=request.POST.get('user_id')
        )

        user.delete()

        messages.success(
            request,
            "User deleted successfully."
        )

        return redirect('user_view')

    # ==================================================
    # CONTEXT
    # ==================================================
    context = {
        'form': form,
        'users': users,
        'search': search,

        'companies': Company.objects.all(),
        'branches': Branch.objects.all(),
        'departments': Department.objects.all(),
        'positions': Position.objects.all(),
    }

    return render(
        request,
        'manager/user.html',
        context
    )
# =========================
# USER DETAIL VIEW
# =========================
def user_detail_view(request, pk):

    user = get_object_or_404(
        User.objects.select_related(
            'company',
            'branch',
            'department',
            'position'
        ),
        pk=pk
    )

    context = {
        'user_detail': user
    }

    return render(
        request,
        'manager/user_detail.html',
        context
    )

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        messages.error(request,'You must login first to access the page')
        return redirect('login')