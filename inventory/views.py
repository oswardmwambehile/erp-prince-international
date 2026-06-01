from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import Product

from .forms import (
    ProductForm,
    CategoryForm,
    UnitForm
)


# =========================
# PRODUCT LIST
# =========================
def product_list(request):

    products = Product.objects.all().order_by("-id")

    return render(
        request,
        "manager/product_list.html",
        {
            "products": products
        }
    )


# =========================
# CREATE PRODUCT
# =========================
def product_create(request):

    product_form = ProductForm()
    category_form = CategoryForm()
    unit_form = UnitForm()

    if request.method == "POST":

        # ADD CATEGORY
        if "save_category" in request.POST:

            category_form = CategoryForm(request.POST)

            if category_form.is_valid():

                category_form.save()

                return redirect("product_create")

        # ADD UNIT
        elif "save_unit" in request.POST:

            unit_form = UnitForm(request.POST)

            if unit_form.is_valid():

                unit_form.save()

                return redirect("product_create")

        # ADD PRODUCT
        else:

            product_form = ProductForm(request.POST)

            if product_form.is_valid():

                product_form.save()

                return redirect("product_list")

    context = {

        "product_form": product_form,
        "category_form": category_form,
        "unit_form": unit_form,
    }

    return render(
        request,
        "manager/product_create.html",
        context
    )


# =========================
# PRODUCT DETAIL
# =========================
def product_detail(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    return render(
        request,
        "manager/product_detail.html",
        {
            "product": product
        }
    )


# =========================
# UPDATE PRODUCT
# =========================
def product_update(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    form = ProductForm(
        request.POST or None,
        instance=product
    )

    if form.is_valid():

        form.save()

        return redirect(
            "inventory:product_detail",
            pk=product.pk
        )

    return render(
        request,
        "manager/product_create.html",
        {
            "form": form,
            "product": product
        }
    )


# =========================
# DELETE PRODUCT
# =========================
def product_delete(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    if request.method == "POST":

        product.delete()

        return redirect(
            "inventory:product_list"
        )

    return render(
        request,
        "manager/products/product_delete.html",
        {
            "product": product
        }
    )
# =========================
# PRODUCT LIST
# =========================
def inventory_product_list(request):

    products = Product.objects.all().order_by("-id")

    return render(
        request,
        "inventory/product_list.html",
        {
            "products": products
        }
    )
# =========================
# PRODUCT LIST
# =========================
def sales_product_list(request):

    products = Product.objects.all().order_by("-id")

    return render(
        request,
        "sales/product_list.html",
        {
            "products": products
        }
    )


# =========================
# CREATE PRODUCT
# =========================
def inventory_product_create(request):

    product_form = ProductForm()
    category_form = CategoryForm()
    unit_form = UnitForm()

    if request.method == "POST":

        # ADD CATEGORY
        if "save_category" in request.POST:

            category_form = CategoryForm(request.POST)

            if category_form.is_valid():

                category_form.save()

                return redirect("inventory_product_create")

        # ADD UNIT
        elif "save_unit" in request.POST:

            unit_form = UnitForm(request.POST)

            if unit_form.is_valid():

                unit_form.save()

                return redirect("inventory_product_create")

        # ADD PRODUCT
        else:

            product_form = ProductForm(request.POST)

            if product_form.is_valid():

                product_form.save()

                return redirect("product_list")

    context = {

        "product_form": product_form,
        "category_form": category_form,
        "unit_form": unit_form,
    }

    return render(
        request,
        "inventory/product_create.html",
        context
    )


# =========================
# PRODUCT DETAIL
# =========================
def inventory_product_detail(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    return render(
        request,
        "inventory/product_detail.html",
        {
            "product": product
        }
    )


def sales_product_detail(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    return render(
        request,
        "sales/product_detail.html",
        {
            "product": product
        }
    )

# =========================
# UPDATE PRODUCT
# =========================
def product_update(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    product_form = ProductForm(
        request.POST or None,
        instance=product
    )

    category_form = CategoryForm()
    unit_form = UnitForm()

    if product_form.is_valid():

        product_form.save()

        return redirect(
            "product_list"
            
        )

    return render(
        request,
        "manager/product_create.html",
        {
            "product_form": product_form,
            "category_form": category_form,
            "unit_form": unit_form,
            "product": product,
            "is_update": True,
        }
    )

# =========================
# DELETE PRODUCT
# =========================
def product_delete(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    product.delete()

    return redirect(
        "product_list"
    )

from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm

def category_page(request):

    categories = Category.objects.all().order_by('-id')
    form = CategoryForm()

    # ---------------- CREATE ----------------
    if request.method == "POST" and "create_category" in request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_page')

    # ---------------- UPDATE ----------------
    if request.method == "POST" and "update_category" in request.POST:
        category_id = request.POST.get("category_id")
        category = get_object_or_404(Category, id=category_id)

        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_page')

    # ---------------- DELETE ----------------
    if request.method == "POST" and "delete_category" in request.POST:
        category_id = request.POST.get("category_id")
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return redirect('category_page')

    return render(request, "inventory/category.html", {
        "categories": categories,
        "form": form
    })

def admin_category_page(request):

    categories = Category.objects.all().order_by('-id')
    form = CategoryForm()

    # ---------------- CREATE ----------------
    if request.method == "POST" and "create_category" in request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_page')

    # ---------------- UPDATE ----------------
    if request.method == "POST" and "update_category" in request.POST:
        category_id = request.POST.get("category_id")
        category = get_object_or_404(Category, id=category_id)

        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_page')

    # ---------------- DELETE ----------------
    if request.method == "POST" and "delete_category" in request.POST:
        category_id = request.POST.get("category_id")
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return redirect('category_page')

    return render(request, "manager/category.html", {
        "categories": categories,
        "form": form
    })


from django.shortcuts import render, redirect, get_object_or_404
from .models import Unit
from .forms import UnitForm


def unit_page(request):

    units = Unit.objects.all().order_by('-id')
    form = UnitForm()

    # ---------------- CREATE ----------------
    if request.method == "POST" and "create_unit" in request.POST:
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_page')

    # ---------------- UPDATE ----------------
    if request.method == "POST" and "update_unit" in request.POST:
        unit_id = request.POST.get("unit_id")
        unit = get_object_or_404(Unit, id=unit_id)

        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('unit_page')

    # ---------------- DELETE ----------------
    if request.method == "POST" and "delete_unit" in request.POST:
        unit_id = request.POST.get("unit_id")
        unit = get_object_or_404(Unit, id=unit_id)
        unit.delete()
        return redirect('unit_page')

    return render(request, 'inventory/unit_page.html', {
        'units': units,
        'form': form
    })

def admin_unit_page(request):

    units = Unit.objects.all().order_by('-id')
    form = UnitForm()

    # ---------------- CREATE ----------------
    if request.method == "POST" and "create_unit" in request.POST:
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unit_page')

    # ---------------- UPDATE ----------------
    if request.method == "POST" and "update_unit" in request.POST:
        unit_id = request.POST.get("unit_id")
        unit = get_object_or_404(Unit, id=unit_id)

        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('unit_page')

    # ---------------- DELETE ----------------
    if request.method == "POST" and "delete_unit" in request.POST:
        unit_id = request.POST.get("unit_id")
        unit = get_object_or_404(Unit, id=unit_id)
        unit.delete()
        return redirect('unit_page')

    return render(request, 'manager/unit_page.html', {
        'units': units,
        'form': form
    })


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Warehouse
from .forms import WarehouseForm


# =====================================================
# WAREHOUSE MANAGEMENT
# =====================================================

def warehouse_list(request):

    warehouses = Warehouse.objects.select_related(
        'manager'
    ).all().order_by('-id')

    form = WarehouseForm()


    # =================================================
    # CREATE WAREHOUSE
    # =================================================
    if request.method == 'POST' and 'create_warehouse' in request.POST:

        form = WarehouseForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Warehouse created successfully.'
            )

            return redirect('warehouse_list')

        else:

            messages.error(
                request,
                'Please correct the errors below.'
            )


    # =================================================
    # UPDATE WAREHOUSE
    # =================================================
    if request.method == 'POST' and 'update_warehouse' in request.POST:

        warehouse_id = request.POST.get('warehouse_id')

        warehouse = get_object_or_404(
            Warehouse,
            id=warehouse_id
        )

        form = WarehouseForm(
            request.POST,
            instance=warehouse
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Warehouse updated successfully.'
            )

            return redirect('warehouse_list')

        else:

            messages.error(
                request,
                'Failed to update warehouse.'
            )


    # =================================================
    # DELETE WAREHOUSE
    # =================================================
    if request.method == 'POST' and 'delete_warehouse' in request.POST:

        warehouse_id = request.POST.get('warehouse_id')

        warehouse = get_object_or_404(
            Warehouse,
            id=warehouse_id
        )

        warehouse.delete()

        messages.success(
            request,
            'Warehouse deleted successfully.'
        )

        return redirect('warehouse_list')


    # =================================================
    # CONTEXT
    # =================================================
    context = {
        'warehouses': warehouses,
        'form': form,
    }

    return render(
        request,
        'manager/warehouse_list.html',
        context
    )

def inventory_warehouse_list(request):

    warehouses = Warehouse.objects.select_related(
        'manager'
    ).all().order_by('-id')

    form = WarehouseForm()


    # =================================================
    # CREATE WAREHOUSE
    # =================================================
    if request.method == 'POST' and 'inventory_create_warehouse' in request.POST:

        form = WarehouseForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Warehouse created successfully.'
            )

            return redirect('warehouse_list')

        else:

            messages.error(
                request,
                'Please correct the errors below.'
            )


    # =================================================
    # UPDATE WAREHOUSE
    # =================================================
    if request.method == 'POST' and 'inventory_update_warehouse' in request.POST:

        warehouse_id = request.POST.get('warehouse_id')

        warehouse = get_object_or_404(
            Warehouse,
            id=warehouse_id
        )

        form = WarehouseForm(
            request.POST,
            instance=warehouse
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Warehouse updated successfully.'
            )

            return redirect('warehouse_list')

        else:

            messages.error(
                request,
                'Failed to update warehouse.'
            )


    # =================================================
    # DELETE WAREHOUSE
    # =================================================
    if request.method == 'POST' and 'inventory_delete_warehouse' in request.POST:

        warehouse_id = request.POST.get('warehouse_id')

        warehouse = get_object_or_404(
            Warehouse,
            id=warehouse_id
        )

        warehouse.delete()

        messages.success(
            request,
            'Warehouse deleted successfully.'
        )

        return redirect('warehouse_list')


    # =================================================
    # CONTEXT
    # =================================================
    context = {
        'warehouses': warehouses,
        'form': form,
    }

    return render(
        request,
        'inventory/warehouse_list.html',
        context
    )

from django.shortcuts import render
from .models import Stock


def stock_list(request):

    stocks = Stock.objects.select_related(
        'product',
        'warehouse'
    ).all()

    return render(request, 'manager/stock_list.html', {
        'stocks': stocks
    })

def inventory_stock_list(request):

    stocks = Stock.objects.select_related(
        'product',
        'warehouse'
    ).all()

    return render(request, 'inventory/stock_list.html', {
        'stocks': stocks
    })

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Stock, StockMovement
from .forms import StockInForm


def stock_in(request):

    form = StockInForm(request.POST or None)

    if form.is_valid():

        product = form.cleaned_data['product']
        warehouse = form.cleaned_data['warehouse']
        quantity = form.cleaned_data['quantity']

        # STEP 1: CREATE OR GET STOCK ROW
        stock, created = Stock.objects.get_or_create(
            product=product,
            warehouse=warehouse,
            defaults={'quantity': 0}
        )

        # STEP 2: ADD QUANTITY
        stock.quantity += quantity
        stock.save()

        # STEP 3: SAVE MOVEMENT HISTORY
        StockMovement.objects.create(
            product=product,
            warehouse=warehouse,
            movement_type='IN',
            quantity=quantity,
            balance_after=stock.quantity,
            created_by=request.user
        )

        messages.success(request, "Stock added successfully!")

        return redirect('stock_list')

    return render(request, 'manager/stock_in.html', {
        'form': form
    })

def inventory_stock_in(request):

    form = StockInForm(request.POST or None)

    if form.is_valid():

        product = form.cleaned_data['product']
        warehouse = form.cleaned_data['warehouse']
        quantity = form.cleaned_data['quantity']

        # STEP 1: CREATE OR GET STOCK ROW
        stock, created = Stock.objects.get_or_create(
            product=product,
            warehouse=warehouse,
            defaults={'quantity': 0}
        )

        # STEP 2: ADD QUANTITY
        stock.quantity += quantity
        stock.save()

        # STEP 3: SAVE MOVEMENT HISTORY
        StockMovement.objects.create(
            product=product,
            warehouse=warehouse,
            movement_type='IN',
            quantity=quantity,
            balance_after=stock.quantity,
            created_by=request.user
        )

        messages.success(request, "Stock added successfully!")

        return redirect('inventory_stock_list')

    return render(request, 'inventory/stock_in.html', {
        'form': form
    })

from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction

from .models import Stock, StockMovement
from .forms import StockOutForm


def stock_out(request):

    form = StockOutForm(request.POST or None)

    if form.is_valid():

        product = form.cleaned_data['product']
        warehouse = form.cleaned_data['warehouse']
        quantity = form.cleaned_data['quantity']
        reference_type = form.cleaned_data.get('reference_type')
        reference_id = form.cleaned_data.get('reference_id')

        stock = Stock.objects.filter(
            product=product,
            warehouse=warehouse
        ).first()

        # SAFETY CHECK (extra protection)
        if not stock:
            messages.error(request, "Stock not found in this warehouse.")
            return redirect('stock_list')

        if stock.quantity < quantity:
            messages.error(request, f"Only {stock.quantity} items available.")
            return redirect('stock_list')

        # TRANSACTION (VERY IMPORTANT)
        with transaction.atomic():

            # 1. Reduce stock
            stock.quantity -= quantity
            stock.save()

            # 2. Save movement log
            StockMovement.objects.create(
                product=product,
                warehouse=warehouse,
                movement_type='OUT',
                quantity=quantity,
                balance_after=stock.quantity,
                reference_type=reference_type,
                reference_id=reference_id,
                created_by=request.user
            )

        messages.success(request, "Stock removed successfully!")

        return redirect('stock_list')

    return render(request, 'manager/stock_out.html', {
        'form': form
    })

def inventory_stock_out(request):

    form = StockOutForm(request.POST or None)

    if form.is_valid():

        product = form.cleaned_data['product']
        warehouse = form.cleaned_data['warehouse']
        quantity = form.cleaned_data['quantity']
        reference_type = form.cleaned_data.get('reference_type')
        reference_id = form.cleaned_data.get('reference_id')

        stock = Stock.objects.filter(
            product=product,
            warehouse=warehouse
        ).first()

        # SAFETY CHECK (extra protection)
        if not stock:
            messages.error(request, "Stock not found in this warehouse.")
            return redirect('stock_list')

        if stock.quantity < quantity:
            messages.error(request, f"Only {stock.quantity} items available.")
            return redirect('stock_list')

        # TRANSACTION (VERY IMPORTANT)
        with transaction.atomic():

            # 1. Reduce stock
            stock.quantity -= quantity
            stock.save()

            # 2. Save movement log
            StockMovement.objects.create(
                product=product,
                warehouse=warehouse,
                movement_type='OUT',
                quantity=quantity,
                balance_after=stock.quantity,
                reference_type=reference_type,
                reference_id=reference_id,
                created_by=request.user
            )

        messages.success(request, "Stock removed successfully!")

        return redirect('inventory_stock_list')

    return render(request, 'inventory/stock_out.html', {
        'form': form
    })


from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction

from .models import Stock, StockMovement
from .forms import StockTransferForm


def stock_transfer(request):

    form = StockTransferForm(request.POST or None)

    if form.is_valid():

        product = form.cleaned_data['product']
        from_warehouse = form.cleaned_data['from_warehouse']
        to_warehouse = form.cleaned_data['to_warehouse']
        quantity = form.cleaned_data['quantity']
        reference_type = form.cleaned_data.get('reference_type')
        reference_id = form.cleaned_data.get('reference_id')

        # GET SOURCE STOCK
        from_stock = Stock.objects.filter(
            product=product,
            warehouse=from_warehouse
        ).first()

        if not from_stock:
            messages.error(request, "No stock in source warehouse.")
            return redirect('stock_list')

        if from_stock.quantity < quantity:
            messages.error(request, f"Only {from_stock.quantity} available.")
            return redirect('stock_list')

        # TRANSACTION SAFETY
        with transaction.atomic():

            # 1. REDUCE FROM SOURCE
            from_stock.quantity -= quantity
            from_stock.save()

            # 2. ADD TO DESTINATION (CREATE IF NOT EXISTS)
            to_stock, created = Stock.objects.get_or_create(
                product=product,
                warehouse=to_warehouse,
                defaults={'quantity': 0}
            )

            to_stock.quantity += quantity
            to_stock.save()

            # 3. LOG MOVEMENT
            StockMovement.objects.create(
                product=product,
                warehouse=from_warehouse,
                movement_type='TRANSFER_OUT',
                quantity=quantity,
                balance_after=from_stock.quantity,
                reference_type=reference_type,
                reference_id=reference_id,
                created_by=request.user
            )

            StockMovement.objects.create(
                product=product,
                warehouse=to_warehouse,
                movement_type='TRANSFER_IN',
                quantity=quantity,
                balance_after=to_stock.quantity,
                reference_type=reference_type,
                reference_id=reference_id,
                created_by=request.user
            )

        messages.success(request, "Stock transferred successfully!")

        return redirect('stock_list')

    return render(request, 'manager/stock_transfer.html', {
        'form': form
    })


def inventory_stock_transfer(request):

    form = StockTransferForm(request.POST or None)

    if form.is_valid():

        product = form.cleaned_data['product']
        from_warehouse = form.cleaned_data['from_warehouse']
        to_warehouse = form.cleaned_data['to_warehouse']
        quantity = form.cleaned_data['quantity']
        reference_type = form.cleaned_data.get('reference_type')
        reference_id = form.cleaned_data.get('reference_id')

        # GET SOURCE STOCK
        from_stock = Stock.objects.filter(
            product=product,
            warehouse=from_warehouse
        ).first()

        if not from_stock:
            messages.error(request, "No stock in source warehouse.")
            return redirect('stock_list')

        if from_stock.quantity < quantity:
            messages.error(request, f"Only {from_stock.quantity} available.")
            return redirect('stock_list')

        # TRANSACTION SAFETY
        with transaction.atomic():

            # 1. REDUCE FROM SOURCE
            from_stock.quantity -= quantity
            from_stock.save()

            # 2. ADD TO DESTINATION (CREATE IF NOT EXISTS)
            to_stock, created = Stock.objects.get_or_create(
                product=product,
                warehouse=to_warehouse,
                defaults={'quantity': 0}
            )

            to_stock.quantity += quantity
            to_stock.save()

            # 3. LOG MOVEMENT
            StockMovement.objects.create(
                product=product,
                warehouse=from_warehouse,
                movement_type='TRANSFER_OUT',
                quantity=quantity,
                balance_after=from_stock.quantity,
                reference_type=reference_type,
                reference_id=reference_id,
                created_by=request.user
            )

            StockMovement.objects.create(
                product=product,
                warehouse=to_warehouse,
                movement_type='TRANSFER_IN',
                quantity=quantity,
                balance_after=to_stock.quantity,
                reference_type=reference_type,
                reference_id=reference_id,
                created_by=request.user
            )

        messages.success(request, "Stock transferred successfully!")

        return redirect('inventory_stock_list')

    return render(request, 'inventory/stock_transfer.html', {
        'form': form
    })


from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction

from .models import Stock, StockMovement
from .forms import StockAdjustmentForm


def stock_adjustment(request):

    form = StockAdjustmentForm(request.POST or None)

    if form.is_valid():

        product = form.cleaned_data['product']
        warehouse = form.cleaned_data['warehouse']
        new_quantity = form.cleaned_data['quantity']
        reason = form.cleaned_data.get('reason')
        reference_type = form.cleaned_data.get('reference_type')
        reference_id = form.cleaned_data.get('reference_id')

        stock = Stock.objects.filter(
            product=product,
            warehouse=warehouse
        ).first()

        if not stock:
            messages.error(request, "Stock not found.")
            return redirect('stock_list')

        with transaction.atomic():

            old_quantity = stock.quantity

            # ✅ SAFETY CHECK (NO NEGATIVE STOCK ALLOWED)
            if new_quantity < 0:
                messages.error(request, "Stock cannot be negative.")
                return redirect('stock_list')

            # ✅ UPDATE STOCK
            stock.quantity = new_quantity
            stock.save()

            # ✅ CALCULATE DIFFERENCE (FOR LOGGING)
            difference = new_quantity - old_quantity

            # ✅ LOG MOVEMENT (AUDIT TRAIL)
            StockMovement.objects.create(
                product=product,
                warehouse=warehouse,
                movement_type='ADJUSTMENT',
                quantity=difference,
                balance_after=new_quantity,
                reference_type=reference_type or "ADJUSTMENT",
                reference_id=reference_id or None,
                created_by=request.user,
                note=reason
            )

        messages.success(request, "Stock adjusted successfully!")
        return redirect('stock_list')

    return render(request, 'manager/stock_adjustment.html', {
        'form': form
    })

def inventory_stock_adjustment(request):

    form = StockAdjustmentForm(request.POST or None)

    if form.is_valid():

        product = form.cleaned_data['product']
        warehouse = form.cleaned_data['warehouse']
        new_quantity = form.cleaned_data['quantity']
        reason = form.cleaned_data.get('reason')
        reference_type = form.cleaned_data.get('reference_type')
        reference_id = form.cleaned_data.get('reference_id')

        stock = Stock.objects.filter(
            product=product,
            warehouse=warehouse
        ).first()

        if not stock:
            messages.error(request, "Stock not found.")
            return redirect('stock_list')

        with transaction.atomic():

            old_quantity = stock.quantity

            # ✅ SAFETY CHECK (NO NEGATIVE STOCK ALLOWED)
            if new_quantity < 0:
                messages.error(request, "Stock cannot be negative.")
                return redirect('stock_list')

            # ✅ UPDATE STOCK
            stock.quantity = new_quantity
            stock.save()

            # ✅ CALCULATE DIFFERENCE (FOR LOGGING)
            difference = new_quantity - old_quantity

            # ✅ LOG MOVEMENT (AUDIT TRAIL)
            StockMovement.objects.create(
                product=product,
                warehouse=warehouse,
                movement_type='ADJUSTMENT',
                quantity=difference,
                balance_after=new_quantity,
                reference_type=reference_type or "ADJUSTMENT",
                reference_id=reference_id or None,
                created_by=request.user,
                note=reason
            )

        messages.success(request, "Stock adjusted successfully!")
        return redirect('inventory_stock_list')

    return render(request, 'inventory/stock_adjustment.html', {
        'form': form
    })



from django.shortcuts import render
from django.db.models import Q

from .models import StockMovement


def stock_movements(request):

    query = request.GET.get('q', '')

    movements = StockMovement.objects.select_related(
        'product', 'warehouse'
    ).order_by('-id')

    # 🔍 SEARCH FILTER
    if query:
        movements = movements.filter(
            Q(product__name__icontains=query) |
            Q(warehouse__name__icontains=query) |
            Q(movement_type__icontains=query)
        )

    return render(request, 'manager/stock_movements.html', {
        'movements': movements,
        'query': query
    })

def inventory_stock_movements(request):

    query = request.GET.get('q', '')

    movements = StockMovement.objects.select_related(
        'product', 'warehouse'
    ).order_by('-id')

    # 🔍 SEARCH FILTER
    if query:
        movements = movements.filter(
            Q(product__name__icontains=query) |
            Q(warehouse__name__icontains=query) |
            Q(movement_type__icontains=query)
        )

    return render(request, 'inventory/stock_movements.html', {
        'movements': movements,
        'query': query
    })



from django.shortcuts import render
from django.db.models import F
from .models import Stock

def low_stock_list(request):

    low_stock_items = Stock.objects.select_related(
        'product', 'warehouse'
    ).filter(
        quantity__lte=F('product__minimum_stock')
    )

    return render(request, 'manager/low_stock.html', {
        'low_stock_items': low_stock_items
    })




from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import ExtractMonth

from .models import (
    Product,
    Warehouse,
    Stock,
    StockMovement
)


def inventory_dashboard(request):

    # ======================================
    # TOTAL PRODUCTS
    # ======================================
    total_products = Product.objects.count()

    # ======================================
    # TOTAL STOCK
    # ======================================
    total_stock = Stock.objects.aggregate(
        total=Sum('quantity')
    )['total'] or 0

    # ======================================
    # TOTAL WAREHOUSES
    # ======================================
    total_warehouses = Warehouse.objects.count()

    # ======================================
    # LOW STOCK PRODUCTS
    # ======================================
    low_stock_products = 0

    products = Product.objects.all()

    for product in products:

        stock_qty = Stock.objects.filter(
            product=product
        ).aggregate(
            total=Sum('quantity')
        )['total'] or 0

        if stock_qty <= product.minimum_stock:
            low_stock_products += 1

    # ======================================
    # STOCK MOVEMENT COUNTS
    # ======================================
    stock_in_count = StockMovement.objects.filter(
        movement_type='IN'
    ).count()

    stock_out_count = StockMovement.objects.filter(
        movement_type='OUT'
    ).count()

    adjustment_count = StockMovement.objects.filter(
        movement_type='ADJUSTMENT'
    ).count()

    transfer_count = StockMovement.objects.filter(
        movement_type='TRANSFER'
    ).count()

    # ======================================
    # RECENT MOVEMENTS
    # ======================================
    recent_movements = StockMovement.objects.select_related(
        'product',
        'warehouse'
    ).order_by('-created_at')[:5]

    # ======================================
    # MONTHLY CHART DATA
    # ======================================
    months = [
        'Jan',
        'Feb',
        'Mar',
        'Apr',
        'May',
        'Jun',
        'Jul',
        'Aug',
        'Sep',
        'Oct',
        'Nov',
        'Dec'
    ]

    stock_in_data = []
    stock_out_data = []

    for month in range(1, 13):

        stock_in_total = StockMovement.objects.filter(
            movement_type='IN',
            created_at__month=month
        ).aggregate(
            total=Sum('quantity')
        )['total'] or 0

        stock_out_total = StockMovement.objects.filter(
            movement_type='OUT',
            created_at__month=month
        ).aggregate(
            total=Sum('quantity')
        )['total'] or 0

        stock_in_data.append(stock_in_total)
        stock_out_data.append(stock_out_total)

    # ======================================
    # CONTEXT
    # ======================================
    context = {

        'total_products': total_products,
        'total_stock': total_stock,
        'total_warehouses': total_warehouses,
        'low_stock_products': low_stock_products,

        'stock_in_count': stock_in_count,
        'stock_out_count': stock_out_count,
        'adjustment_count': adjustment_count,
        'transfer_count': transfer_count,

        'recent_movements': recent_movements,

        'months': months,
        'stock_in_data': stock_in_data,
        'stock_out_data': stock_out_data,
    }

    return render(
        request,
        'inventory/home_inventory.html',
        context
    )

