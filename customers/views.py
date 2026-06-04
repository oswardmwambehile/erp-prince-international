from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Customer
from .forms import CustomerForm


# =========================
# CUSTOMER LIST
# =========================
def customer_list(request):

    customers = Customer.objects.all().order_by('-id')

    context = {
        'customers': customers
    }

    return render(
        request,
        'manager/customer_list.html',
        context
    )
# =========================
# CUSTOMER LIST
# =========================
def sales_customer_list(request):

    customers = Customer.objects.all().order_by('-id')

    context = {
        'customers': customers
    }

    return render(
        request,
        'sales/customer_list.html',
        context
    )


# =========================
# CUSTOMER CREATE
# =========================
def customer_create(request):

    if request.method == 'POST':

        form = CustomerForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Customer created successfully.'
            )

            return redirect('customer_list')

    else:
        form = CustomerForm()

    context = {
        'form': form
    }

    return render(
        request,
        'manager/customer_form.html',
        context
    )
# =========================
# CUSTOMER CREATE
# =========================
def sales_customer_create(request):

    if request.method == 'POST':

        form = CustomerForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Customer created successfully.'
            )

            return redirect('sales_customer_list')

    else:
        form = CustomerForm()

    context = {
        'form': form
    }

    return render(
        request,
        'sales/customer_form.html',
        context
    )


# =========================
# CUSTOMER DETAIL
# =========================
def customer_detail(request, pk):

    customer = get_object_or_404(
        Customer,
        pk=pk
    )

    context = {
        'customer': customer
    }

    return render(
        request,
        'manager/customer_detail.html',
        context
    )
# =========================
# CUSTOMER DETAIL
# =========================
def sales_customer_detail(request, pk):

    customer = get_object_or_404(
        Customer,
        pk=pk
    )

    context = {
        'customer': customer
    }

    return render(
        request,
        'sales/customer_detail.html',
        context
    )


# =========================
# CUSTOMER UPDATE
# =========================
def customer_update(request, pk):

    customer = get_object_or_404(
        Customer,
        pk=pk
    )

    if request.method == 'POST':

        form = CustomerForm(
            request.POST,
            instance=customer
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Customer updated successfully.'
            )

            return redirect(
                'customer_list'
            )

    else:

        form = CustomerForm(
            instance=customer
        )

    context = {
        'form': form,
        'customer': customer
    }

    return render(
        request,
        'manager/customer_form.html',
        context
    )

def sales_customer_update(request, pk):

    customer = get_object_or_404(
        Customer,
        pk=pk
    )

    if request.method == 'POST':

        form = CustomerForm(
            request.POST,
            instance=customer
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Customer updated successfully.'
            )

            return redirect(
                'sales_customer_list'
            )

    else:

        form = CustomerForm(
            instance=customer
        )

    context = {
        'form': form,
        'customer': customer
    }

    return render(
        request,
        'sales/customer_form.html',
        context
    )



# DELETE CUSTOMER
# =========================
def customer_delete(request, pk):

    customer = get_object_or_404(
        Customer,
        pk=pk
    )

    customer.delete()

    messages.success(
        request,
        'Customer deleted successfully.'
    )

    return redirect(
        'customer_list'
    )


from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import Supplier
from .forms import SupplierForm


# =========================
# LIST
# =========================
def supplier_list(request):

    suppliers = Supplier.objects.all().order_by('-id')

    context = {
        'suppliers': suppliers
    }

    return render(
        request,
        'manager/supplier_list.html',
        context
    )


# =========================
# CREATE
# =========================
def supplier_create(request):

    form = SupplierForm(request.POST or None)

    if form.is_valid():

        form.save()

        messages.success(
            request,
            'Supplier created successfully.'
        )

        return redirect('supplier_list')

    context = {
        'form': form
    }

    return render(
        request,
        'manager/supplier_form.html',
        context
    )


# =========================
# UPDATE
# =========================
def supplier_update(request, pk):

    supplier = get_object_or_404(
        Supplier,
        pk=pk
    )

    form = SupplierForm(
        request.POST or None,
        instance=supplier
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            'Supplier updated successfully.'
        )

        return redirect('supplier_list')

    context = {
        'form': form,
        'supplier': supplier
    }

    return render(
        request,
        'manager/supplier_form.html',
        context
    )


# =========================
# DETAIL
# =========================
def supplier_detail(request, pk):

    supplier = get_object_or_404(
        Supplier,
        pk=pk
    )

    context = {
        'supplier': supplier
    }

    return render(
        request,
        'manager/supplier_detail.html',
        context
    )


# =========================
# DELETE
# =========================
def supplier_delete(request, pk):

    supplier = get_object_or_404(
        Supplier,
        pk=pk
    )

    supplier.delete()

    messages.success(
        request,
        'Supplier deleted successfully.'
    )

    return redirect('supplier_list')