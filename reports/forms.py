from django import forms
from django.forms import inlineformset_factory

from .models import QuotationNormal, QuotationItemNormal


# ==========================
# QUOTATION FORM
# ==========================
class QuotationFormNormal(forms.ModelForm):

    class Meta:
        model = QuotationNormal
        fields = [
            "quotation_no",
            "customer",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        base_class = (
            "w-full px-4 py-3 border border-gray-300 "
            "rounded-xl focus:ring-2 focus:ring-green-500 "
            "focus:border-green-500 focus:outline-none"
        )

        for field in self.fields.values():
            field.widget.attrs["class"] = base_class

        self.fields["quotation_no"].widget.attrs["placeholder"] = "QT-000001"

        self.fields["customer"].label_from_instance = (
            lambda obj: getattr(obj, "company_name", None)
            or getattr(obj, "name", None)
            or str(obj)
        )


# ==========================
# QUOTATION ITEM FORM
# ==========================
class QuotationItemFormNormal(forms.ModelForm):

    class Meta:
        model = QuotationItemNormal
        fields = [
            "product",
            "quantity",
            "unit_price",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        base_class = (
            "w-full px-4 py-3 border border-gray-300 "
            "rounded-xl focus:ring-2 focus:ring-green-500 "
            "focus:border-green-500 focus:outline-none"
        )

        for field in self.fields.values():
            field.widget.attrs["class"] = base_class

        self.fields["quantity"].widget.attrs["placeholder"] = "Quantity"

        self.fields["unit_price"].widget.attrs["placeholder"] = "Unit Price"

        self.fields["product"].label_from_instance = (
            lambda obj: f"{obj.name} ({obj.code})"
            if hasattr(obj, "code")
            else obj.name
        )


# ==========================
# FORMSET
# ==========================
QuotationItemFormSet = inlineformset_factory(
    QuotationNormal,
    QuotationItemNormal,
    form=QuotationItemFormNormal,
    extra=1,
    can_delete=True,
)