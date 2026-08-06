from django.shortcuts import render, redirect
from django.contrib import messages

from .models import QuotationNormal
from .forms import (
    QuotationFormNormal,
    QuotationItemFormSet,
)


def quotation_create(request):

    if request.method == "POST":

        form = QuotationFormNormal(request.POST)
        formset = QuotationItemFormSet(request.POST)

        if form.is_valid() and formset.is_valid():

            quotation = form.save()

            formset.instance = quotation
            formset.save()

            messages.success(request, "Quotation Created Successfully")

            return redirect("quotation_list")

    else:

        form = QuotationFormNormal()
        formset = QuotationItemFormSet()

    context = {
        "form": form,
        "formset": formset,
    }

    return render(request, "sales/quotation_form.html", context)



from django.shortcuts import render
from .models import QuotationNormal


def normal_quotation_list(request):

    quotations = QuotationNormal.objects.all().order_by("-id")

    context = {
        "quotations": quotations,
        "page_title": "Quotation List",
    }

    return render(
        request,
        "sales/normal_quotation_list.html",
        context
    )


from django.shortcuts import render, get_object_or_404

from .models import QuotationNormal


def normal_quotation_detail(request, pk):

    quotation = get_object_or_404(
        QuotationNormal,
        pk=pk
    )

    items = quotation.items.all()

    context = {
        "quotation": quotation,
        "items": items,
        "page_title": "Quotation Detail",
    }

    return render(
        request,
        "sales/normal_quotation_detail.html",
        context
    )


from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from django.shortcuts import get_object_or_404

from xhtml2pdf import pisa

import os

from .models import QuotationNormal



def quotation_pdf(request, pk):

    quotation = get_object_or_404(
        QuotationNormal,
        pk=pk
    )


    template = get_template(
        "sales/normal-quotation_pdf.html"
    )


    # ==========================
    # COMPANY LOGO PATH
    # ==========================

    logo_path = os.path.join(
        settings.BASE_DIR,
        "static",
        "img",
        "prince.jpeg"
    )

    logo_paths = os.path.join(
        settings.BASE_DIR,
        "static",
        "img",
        "qr-codes.png"
    )



    html = template.render({

        "quotation": quotation,

        "items": quotation.items.all(),

        "company_logo": logo_path,
        "company_logos": logo_paths,

    })



    response = HttpResponse(
        content_type="application/pdf"
    )


    response["Content-Disposition"] = (
        f'attachment; filename="quotation_{quotation.quotation_no}.pdf"'
    )



    pisa_status = pisa.CreatePDF(

        html,

        dest=response

    )



    if pisa_status.err:

        return HttpResponse(
            "PDF generation error"
        )



    return response