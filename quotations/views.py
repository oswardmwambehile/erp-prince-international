from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.shortcuts import redirect, render

from .forms import QuotationForm, QuotationItemForm
from .models import Quotation, QuotationItem

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory

from .models import Quotation, QuotationItem
from .forms import QuotationForm, QuotationItemForm


QuotationItemFormSet = inlineformset_factory(
    Quotation,
    QuotationItem,
    form=QuotationItemForm,
    extra=1,
    can_delete=True
)


@login_required(login_url='login')
def create_quotation(request):

    quotation_form = QuotationForm(request.POST or None)

    # -----------------------------------
    # INIT EMPTY FORMSET (GET REQUEST)
    # -----------------------------------
    if request.method == "GET":
        item_formset = QuotationItemFormSet(
            instance=Quotation(),
            prefix="items"
        )

        return render(request, "manager/create.html", {
            "quotation_form": quotation_form,
            "item_formset": item_formset,
            "is_update": False,
        })

    # -----------------------------------
    # POST REQUEST
    # -----------------------------------
    item_formset = QuotationItemFormSet(
        request.POST,
        instance=Quotation(),
        prefix="items"
    )

    # DEBUG (optional)
    print(request.POST)

    # -----------------------------------
    # VALIDATE FORMS
    # -----------------------------------
    if quotation_form.is_valid() and item_formset.is_valid():

        quotation = quotation_form.save(commit=False)
        quotation.created_by = request.user
        quotation.save()

        items = item_formset.save(commit=False)

        for item in items:

            # -------------------------------
            # FORCE SAFE DEFAULTS
            # -------------------------------

            item.cts = item.cts or 0
            item.sqm = item.sqm or 0
            item.total_sqm = item.total_sqm or 0
            item.total_price = item.total_price or 0

            # IMPORTANT: attach parent
            item.quotation = quotation

            item.save()

        # handle deleted rows
        item_formset.save_m2m()

        # recalculate quotation totals (if you have it)
        if hasattr(quotation, "calculate_totals"):
            quotation.calculate_totals()

        messages.success(request, "Quotation created successfully")

        return redirect("quotations:quotation_detail", pk=quotation.pk)

    # -----------------------------------
    # DEBUG ERRORS
    # -----------------------------------
    print("FORM ERRORS:", quotation_form.errors)
    print("FORMSET ERRORS:", item_formset.errors)

    messages.error(request, "Please fix the errors below.")

    return render(request, "manager/create.html", {
        "quotation_form": quotation_form,
        "item_formset": item_formset,
        "is_update": False,
    })



@login_required(login_url='login')
def sales_create_quotation(request):

    quotation_form = QuotationForm(request.POST or None)

    # -----------------------------------
    # INIT EMPTY FORMSET (GET REQUEST)
    # -----------------------------------
    if request.method == "GET":
        item_formset = QuotationItemFormSet(
            instance=Quotation(),
            prefix="items"
        )

        return render(request, "sales/create.html", {
            "quotation_form": quotation_form,
            "item_formset": item_formset,
            "is_update": False,
        })

    # -----------------------------------
    # POST REQUEST
    # -----------------------------------
    item_formset = QuotationItemFormSet(
        request.POST,
        instance=Quotation(),
        prefix="items"
    )

    # DEBUG (optional)
    print(request.POST)

    # -----------------------------------
    # VALIDATE FORMS
    # -----------------------------------
    if quotation_form.is_valid() and item_formset.is_valid():

        quotation = quotation_form.save(commit=False)
        quotation.created_by = request.user
        quotation.save()

        items = item_formset.save(commit=False)

        for item in items:

            # -------------------------------
            # FORCE SAFE DEFAULTS
            # -------------------------------

            item.cts = item.cts or 0
            item.sqm = item.sqm or 0
            item.total_sqm = item.total_sqm or 0
            item.total_price = item.total_price or 0

            # IMPORTANT: attach parent
            item.quotation = quotation

            item.save()

        # handle deleted rows
        item_formset.save_m2m()

        # recalculate quotation totals (if you have it)
        if hasattr(quotation, "calculate_totals"):
            quotation.calculate_totals()

        messages.success(request, "Quotation created successfully")

        return redirect("quotations:sales_quotation_detail", pk=quotation.pk)

    # -----------------------------------
    # DEBUG ERRORS
    # -----------------------------------
    print("FORM ERRORS:", quotation_form.errors)
    print("FORMSET ERRORS:", item_formset.errors)

    messages.error(request, "Please fix the errors below.")

    return render(request, "sales/create.html", {
        "quotation_form": quotation_form,
        "item_formset": item_formset,
        "is_update": False,
    })



from decimal import Decimal
from collections import defaultdict

from django.shortcuts import render, get_object_or_404

from .models import Quotation

@login_required(login_url='login')
def quotation_detail(request, pk):

    quotation = get_object_or_404(
        Quotation,
        pk=pk
    )

    # =========================================
    # GROUP ITEMS BY PRODUCT ID
    # =========================================
    grouped_items = defaultdict(list)

    for item in quotation.items.all():

        product_key = (
            item.product.id
            if item.product
            else "unknown"
        )

        grouped_items[product_key].append(item)

    grouped_data = []

    summary_rows = []

    # =========================================
    # GRAND TOTAL VARIABLES
    # =========================================
    total_qty = 0

    total_sqm = Decimal("0.00")

    total_total_sqm = Decimal("0.00")

    total_unit_price = Decimal("0.00")

    total_subtotal = Decimal("0.00")

    # =========================================
    # LOOP GROUPED PRODUCTS
    # =========================================
    for product_id, items in grouped_items.items():

        # PRODUCT NAME
        if items[0].product:
            product_name = str(items[0].product)
        else:
            product_name = "Unknown Product"

        # =========================================
        # SUBTOTALS
        # =========================================
        subtotal_qty = sum(
            item.quantity or 0
            for item in items
        )

        subtotal_sqm = sum(
            item.sqm or Decimal("0.00")
            for item in items
        )

        subtotal_total_sqm = sum(
            item.total_sqm or Decimal("0.00")
            for item in items
        )

        subtotal_unit_price = sum(
            item.unit_price or Decimal("0.00")
            for item in items
        )

        subtotal_total_price = sum(
            item.total_price or Decimal("0.00")
            for item in items
        )

        # =========================================
        # PRODUCT TABLE DATA
        # =========================================
        grouped_data.append({

            "product_name": product_name,

            "items": items,

            "subtotal_qty": subtotal_qty,

            "subtotal_sqm": subtotal_sqm,

            "subtotal_total_sqm": subtotal_total_sqm,

            "subtotal_unit_price": subtotal_unit_price,

            "subtotal_total_price": subtotal_total_price,
        })

        # =========================================
        # SUMMARY TABLE ROWS
        # =========================================
        summary_rows.append({

            "label": product_name,

            "qty": subtotal_qty,

            "sqm": subtotal_sqm,

            "total_sqm": subtotal_total_sqm,

            "unit_price": subtotal_unit_price,

            "value": subtotal_total_price,
        })

        # =========================================
        # FINAL TOTALS
        # =========================================
        total_qty += subtotal_qty

        total_sqm += subtotal_sqm

        total_total_sqm += subtotal_total_sqm

        total_unit_price += subtotal_unit_price

        total_subtotal += subtotal_total_price

    # =========================================
    # VAT
    # =========================================
    if quotation.vat_included:

        vat_amount = (
            total_subtotal *
            quotation.vat_percentage
        ) / Decimal("100")

    else:
        vat_amount = Decimal("0.00")

    # =========================================
    # GRAND TOTAL
    # =========================================
    grand_total = (
        total_subtotal
        + vat_amount
        - quotation.discount_amount
    )

    # =========================================
    # CONTEXT
    # =========================================
    context = {

        "quotation": quotation,

        "grouped_data": grouped_data,

        "summary_rows": summary_rows,

        # TOTALS
        "total_qty": total_qty,

        "total_sqm": total_sqm,

        "total_total_sqm": total_total_sqm,

        "total_unit_price": total_unit_price,

        "total_subtotal": total_subtotal,

        "vat_amount": vat_amount,

        "grand_total": grand_total,
    }

    return render(
        request,
        "manager/quotation_detail.html",
        context
    )


@login_required(login_url='login')
def sales_quotation_detail(request, pk):

    quotation = get_object_or_404(
        Quotation,
        pk=pk
    )

    # =========================================
    # GROUP ITEMS BY PRODUCT ID
    # =========================================
    grouped_items = defaultdict(list)

    for item in quotation.items.all():

        product_key = (
            item.product.id
            if item.product
            else "unknown"
        )

        grouped_items[product_key].append(item)

    grouped_data = []

    summary_rows = []

    # =========================================
    # GRAND TOTAL VARIABLES
    # =========================================
    total_qty = 0

    total_sqm = Decimal("0.00")

    total_total_sqm = Decimal("0.00")

    total_unit_price = Decimal("0.00")

    total_subtotal = Decimal("0.00")

    # =========================================
    # LOOP GROUPED PRODUCTS
    # =========================================
    for product_id, items in grouped_items.items():

        # PRODUCT NAME
        if items[0].product:
            product_name = str(items[0].product)
        else:
            product_name = "Unknown Product"

        # =========================================
        # SUBTOTALS
        # =========================================
        subtotal_qty = sum(
            item.quantity or 0
            for item in items
        )

        subtotal_sqm = sum(
            item.sqm or Decimal("0.00")
            for item in items
        )

        subtotal_total_sqm = sum(
            item.total_sqm or Decimal("0.00")
            for item in items
        )

        subtotal_unit_price = sum(
            item.unit_price or Decimal("0.00")
            for item in items
        )

        subtotal_total_price = sum(
            item.total_price or Decimal("0.00")
            for item in items
        )
        products_list = ", ".join(
        sorted(set(
            str(item.product)
            for item in quotation.items.all()
            if item.product
        ))
    )

        # =========================================
        # PRODUCT TABLE DATA
        # =========================================
        grouped_data.append({

            "product_name": product_name,

            "items": items,

            "subtotal_qty": subtotal_qty,

            "subtotal_sqm": subtotal_sqm,

            "subtotal_total_sqm": subtotal_total_sqm,

            "subtotal_unit_price": subtotal_unit_price,

            "subtotal_total_price": subtotal_total_price,
        })

        # =========================================
        # SUMMARY TABLE ROWS
        # =========================================
        summary_rows.append({

            "label": product_name,

            "qty": subtotal_qty,

            "sqm": subtotal_sqm,

            "total_sqm": subtotal_total_sqm,

            "unit_price": subtotal_unit_price,

            "value": subtotal_total_price,
        })

        # =========================================
        # FINAL TOTALS
        # =========================================
        total_qty += subtotal_qty

        total_sqm += subtotal_sqm

        total_total_sqm += subtotal_total_sqm

        total_unit_price += subtotal_unit_price

        total_subtotal += subtotal_total_price

    # =========================================
    # VAT
    # =========================================
    if quotation.vat_included:

        vat_amount = (
            total_subtotal *
            quotation.vat_percentage
        ) / Decimal("100")

    else:
        vat_amount = Decimal("0.00")

    # =========================================
    # GRAND TOTAL
    # =========================================
    grand_total = (
        total_subtotal
        + vat_amount
        - quotation.discount_amount
    )

    # =========================================
    # CONTEXT
    # =========================================
    context = {

        "quotation": quotation,

        "grouped_data": grouped_data,

        "summary_rows": summary_rows,

        # TOTALS
        "total_qty": total_qty,

        "total_sqm": total_sqm,

        "total_total_sqm": total_total_sqm,

        "total_unit_price": total_unit_price,

        "total_subtotal": total_subtotal,

        "vat_amount": vat_amount,

        "grand_total": grand_total,
        "products_list":products_list
    }

    return render(
        request,
        "sales/quotation_detail.html",
        context
    )




from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Quotation


# =========================================
# QUOTATION LIST
# =========================================
@login_required(login_url='login')
def quotation_list(request):

    quotations = Quotation.objects.select_related(
        'customer',
        'created_by'
    ).order_by('-created_at')

    query = request.GET.get('q')

    if query:

        quotations = quotations.filter(

            Q(quotation_number__icontains=query) |
            Q(customer__name__icontains=query)

        )

    context = {
        'quotations': quotations
    }

    return render(
        request,
        'manager/quotation-list.html',
        context
    )


# =========================================
# QUOTATION LIST
# =========================================
@login_required(login_url='login')
def sales_quotation_list(request):

    quotations = Quotation.objects.select_related(
            'customer',
            'created_by'
        ).filter(
            created_by=request.user
        ).order_by('-created_at')
    query = request.GET.get('q')

    if query:

        quotations = quotations.filter(

            Q(quotation_number__icontains=query) |
            Q(customer__name__icontains=query)

        )

    context = {
        'quotations': quotations
    }

    return render(
        request,
        'sales/quotation-list.html',
        context
    )

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, render, redirect

from .models import Quotation, QuotationItem
from .forms import QuotationForm, QuotationItemForm


QuotationItemFormSet = inlineformset_factory(
    Quotation,
    QuotationItem,
    form=QuotationItemForm,
    extra=0,
    can_delete=True
)


@login_required(login_url='login')
def update_quotation(request, pk):

    quotation = get_object_or_404(Quotation, pk=pk)

    ItemFormSet = inlineformset_factory(
        Quotation,
        QuotationItem,
        form=QuotationItemForm,
        extra=0,
        can_delete=True
    )

    if request.method == "POST":

        quotation_form = QuotationForm(request.POST, instance=quotation)

        item_formset = ItemFormSet(
            request.POST,
            instance=quotation,
            prefix="items"
        )

        # DEBUG
        print("\n========== UPDATE DEBUG ==========")
        print("QUOTATION FORM VALID:", quotation_form.is_valid())
        print("FORMSET VALID:", item_formset.is_valid())

        if not item_formset.is_valid():
            print("FORMSET ERRORS:", item_formset.errors)
            print("NON FORM ERRORS:", item_formset.non_form_errors())

        print("==================================\n")

        if quotation_form.is_valid() and item_formset.is_valid():

            quotation = quotation_form.save()

            # IMPORTANT FIX: use save() directly (DO NOT MANUALLY REASSIGN IDs)
            item_formset.instance = quotation
            item_formset.save()

            quotation.calculate_totals()

            messages.success(request, "Quotation updated successfully")
            return redirect("quotations:quotation_detail", pk=quotation.pk)

    else:
        quotation_form = QuotationForm(instance=quotation)

        item_formset = ItemFormSet(
            instance=quotation,
            prefix="items"
        )

    return render(request, "manager/create.html", {
        "quotation_form": quotation_form,
        "item_formset": item_formset,
        "is_update": True,
    })


@login_required(login_url='login')
def sales_update_quotation(request, pk):

    quotation = get_object_or_404(Quotation, pk=pk)

    ItemFormSet = inlineformset_factory(
        Quotation,
        QuotationItem,
        form=QuotationItemForm,
        extra=0,
        can_delete=True
    )

    if request.method == "POST":

        quotation_form = QuotationForm(request.POST, instance=quotation)

        item_formset = ItemFormSet(
            request.POST,
            instance=quotation,
            prefix="items"
        )

        # DEBUG
        print("\n========== UPDATE DEBUG ==========")
        print("QUOTATION FORM VALID:", quotation_form.is_valid())
        print("FORMSET VALID:", item_formset.is_valid())

        if not item_formset.is_valid():
            print("FORMSET ERRORS:", item_formset.errors)
            print("NON FORM ERRORS:", item_formset.non_form_errors())

        print("==================================\n")

        if quotation_form.is_valid() and item_formset.is_valid():

            quotation = quotation_form.save()

            # IMPORTANT FIX: use save() directly (DO NOT MANUALLY REASSIGN IDs)
            item_formset.instance = quotation
            item_formset.save()

            quotation.calculate_totals()

            messages.success(request, "Quotation updated successfully")
            return redirect("quotations:sales_quotation_detail", pk=quotation.pk)

    else:
        quotation_form = QuotationForm(instance=quotation)

        item_formset = ItemFormSet(
            instance=quotation,
            prefix="items"
        )

    return render(request, "sales/create.html", {
        "quotation_form": quotation_form,
        "item_formset": item_formset,
        "is_update": True,
    })



from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from .models import Quotation


@login_required(login_url='signin')
def delete_quotation(request, pk):

    quotation = get_object_or_404(Quotation, pk=pk)

    # optional safety: allow only POST delete
    if request.method == "POST":

        quotation.delete()

        messages.success(request, "Quotation deleted successfully")

        return redirect("quotations:quotation_list")

    # if someone opens URL directly, just redirect
    return redirect("quotations:quotation_list")



from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from xhtml2pdf import pisa
from io import BytesIO

from decimal import Decimal
from collections import defaultdict

from .models import Quotation
from django.templatetags.static import static
from django.conf import settings


@login_required(login_url='login')
def quotation_pdf(request, pk):

    quotation = get_object_or_404(Quotation, pk=pk)

    # =========================
    # GROUP ITEMS (same logic)
    # =========================
    grouped_items = defaultdict(list)

    for item in quotation.items.all():
        key = item.product.id if item.product else "unknown"
        grouped_items[key].append(item)

    grouped_data = []
    summary_rows = []

    total_qty = 0
    total_subtotal = Decimal("0.00")
    total_sqm = Decimal("0.00")
    total_total_sqm = Decimal("0.00")
    total_unit_price = Decimal("0.00")

    for product_id, items in grouped_items.items():

        product_name = str(items[0].product) if items[0].product else "Unknown"

        subtotal_qty = sum(i.quantity or 0 for i in items)
        subtotal_sqm = sum(i.sqm or 0 for i in items)
        subtotal_total_sqm = sum(i.total_sqm or 0 for i in items)
        subtotal_unit_price = sum(i.unit_price or 0 for i in items)
        subtotal_total_price = sum(i.total_price or 0 for i in items)

        grouped_data.append({
            "product_name": product_name,
            "items": items,
            "subtotal_qty": subtotal_qty,
            "subtotal_sqm": subtotal_sqm,
            "subtotal_total_sqm": subtotal_total_sqm,
            "subtotal_unit_price": subtotal_unit_price,
            "subtotal_total_price": subtotal_total_price,
        })

        summary_rows.append({
            "label": product_name,
            "qty": subtotal_qty,
            "sqm": subtotal_sqm,
            "total_sqm": subtotal_total_sqm,
            "unit_price": subtotal_unit_price,
            "value": subtotal_total_price,
        })

        

        total_qty += subtotal_qty
        total_subtotal += subtotal_total_price
        total_sqm += subtotal_sqm
        total_total_sqm += subtotal_total_sqm
        total_unit_price += subtotal_unit_price

    vat_amount = Decimal("0.00")
    if quotation.vat_included:
        vat_amount = (total_subtotal * quotation.vat_percentage) / Decimal("100")

    grand_total = total_subtotal + vat_amount - quotation.discount_amount
    logo_url = request.build_absolute_uri(static("img/logo.png"))
    logo_urls = request.build_absolute_uri(static("img/logo1.PNG"))
    products_list = ", ".join(
        sorted(set(
            str(item.product)
            for item in quotation.items.all()
            if item.product
        )))

    context = {
        "quotation": quotation,
        "grouped_data": grouped_data,
        "summary_rows": summary_rows,
        "total_qty": total_qty,
        "total_subtotal": total_subtotal,
        "total_sqm": total_sqm,
        "total_total_sqm": total_total_sqm,
        "total_unit_price": total_unit_price,
        "vat_amount": vat_amount,
        "grand_total": grand_total,
        "logo_url":logo_url,
        "logo_urls":logo_urls,
        "products_list":products_list
    }

    # =========================
    # RENDER HTML TEMPLATE
    # =========================
    html_string = render_to_string(
        "manager/quotation_pdf.html",
        context,
        request=request
    )

    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html_string.encode("UTF-8")), result)

    if pdf.err:
        return HttpResponse("Error generating PDF", status=500)

    response = HttpResponse(result.getvalue(), content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="quotation_{quotation.quotation_no}.pdf"'

    return response