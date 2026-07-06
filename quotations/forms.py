from django import forms

from .models import (
    Quotation,
    QuotationItem
)
from decimal import Decimal


# =====================================================
# TAILWIND CLASSES
# =====================================================
TAILWIND_INPUT = (
    "w-full rounded-xl border border-gray-300 "
    "bg-white px-4 py-3 text-sm "
    "focus:border-indigo-500 focus:ring-2 "
    "focus:ring-indigo-200 outline-none"
)

TAILWIND_SELECT = (
    "w-full rounded-xl border border-gray-300 "
    "bg-white px-4 py-3 text-sm "
    "focus:border-indigo-500 focus:ring-2 "
    "focus:ring-indigo-200 outline-none"
)


# =====================================================
# QUOTATION FORM
# =====================================================
class QuotationForm(forms.ModelForm):

    VAT_CHOICES = (
        (True, 'VAT Included'),
        (False, 'VAT Excluded'),
    )

    vat_included = forms.TypedChoiceField(
        choices=VAT_CHOICES,
        coerce=lambda x: x == 'True',
        widget=forms.Select(
            attrs={
                'class': TAILWIND_SELECT
            }
        )
    )

    quotation_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': TAILWIND_INPUT
            }
        )
    )

    class Meta:
        model = Quotation

        fields = [
            'customer',
            
            'project_location',
            'currency',
            
            'quotation_date',
            'vat_included',
            'vat_percentage',
            'discount_amount',
            
        ]

        widgets = {

            'customer': forms.Select(
                attrs={
                    'class': TAILWIND_SELECT
                }
            ),

            'project_name': forms.TextInput(
                attrs={
                    'class': TAILWIND_INPUT,
                    'placeholder': 'Project Name'
                }
            ),
            
             'currency': forms.Select(
                attrs={
                    'class': TAILWIND_SELECT
                }
            ),

            'project_location': forms.TextInput(
                attrs={
                    'class': TAILWIND_INPUT,
                    'placeholder': 'Project Location'
                }
            ),

            'contact_person': forms.TextInput(
                attrs={
                    'class': TAILWIND_INPUT,
                    'placeholder': 'Contact Person'
                }
            ),

            'vat_percentage': forms.NumberInput(
                attrs={
                    'class': TAILWIND_INPUT,
                    'step': '0.01',
                    'placeholder': 'VAT Percentage'
                }
            ),

            'discount_amount': forms.NumberInput(
                attrs={
                    'class': TAILWIND_INPUT,
                    'step': '0.01',
                    'placeholder': 'Discount Amount'
                }
            ),

            'sales_person': forms.Select(
                attrs={
                    'class': TAILWIND_SELECT
                }
            ),
        }


# =====================================================
# QUOTATION ITEM FORM
# =====================================================
# =====================================================
# QUOTATION ITEM FORM
# =====================================================
class QuotationItemForm(forms.ModelForm):

    class Meta:
        model = QuotationItem

        fields = [
            'product',
            'item_code',
            'aluminium_profile',
            'glass',
            'width',
            'height',
            'quantity',
            'sqm',
            'total_sqm',
            'unit_price',
            'total_price',
            'cts',
        ]

        widgets = {

            'product': forms.Select(
                attrs={
                    'class': TAILWIND_SELECT
                }
            ),

            'item_code': forms.TextInput(
                attrs={
                    'class': TAILWIND_INPUT,
                    'placeholder': 'A01'
                }
            ),

            
            'aluminium_profile': forms.Select(
                    attrs={
                        'class': TAILWIND_INPUT,
                    }
                ),

                'glass': forms.Select(
                    attrs={
                        'class': TAILWIND_INPUT,
                    }
                ),
            'width': forms.NumberInput(
                attrs={
                    'class': TAILWIND_INPUT,
                    'step': '0.01',
                    'placeholder': 'Width'
                }
            ),

            'height': forms.NumberInput(
                attrs={
                    'class': TAILWIND_INPUT,
                    'step': '0.01',
                    'placeholder': 'Height'
                }
            ),

            'quantity': forms.NumberInput(
                attrs={
                    'class': TAILWIND_INPUT,
                    'value': '1',
                    'placeholder': 'Quantity'
                }
            ),

            # SQM
            'sqm': forms.NumberInput(
                attrs={
                    'class': TAILWIND_INPUT,
                    'step': '0.1',
                    
                    'placeholder': 'SQM'
                }
            ),

            # TOTAL SQM
            'total_sqm': forms.NumberInput(
                attrs={
                    'class': TAILWIND_INPUT + ' bg-gray-100',
                    'step': '0.1',
                    'readonly': 'readonly',
                    'placeholder': 'Total SQM'
                }
            ),

            'unit_price': forms.NumberInput(
                attrs={
                    'class': TAILWIND_INPUT,
                    'step': '0.01',
                    'placeholder': 'Unit Price'
                }
            ),

            # TOTAL PRICE
            'total_price': forms.NumberInput(
                attrs={
                    'class': TAILWIND_INPUT + ' bg-gray-100',
                    'step': '0.01',
                    'readonly': 'readonly',
                    'placeholder': 'Total Price'
                }
            ),

            'cts': forms.NumberInput(
                attrs={
                    'class': TAILWIND_INPUT,
                    'step': '0.01',
                    'value': '0.00'
                }
            ),
        }

    

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['sqm'].required = False

        self.fields['total_sqm'].required = False

        self.fields['total_price'].required = False

    # =====================================================
    # VALIDATIONS
    # =====================================================
    def clean(self):
            cleaned_data = super().clean()

            width = cleaned_data.get("width") or Decimal("0")
            height = cleaned_data.get("height") or Decimal("0")
            sqm = cleaned_data.get("sqm") or Decimal("0")

            # Either width & height OR sqm must be provided
            if width <= 0 and height <= 0 and sqm <= 0:
                raise forms.ValidationError(
                    "Enter either Width and Height or Square Meter (SQM)."
                )

            # If one dimension is entered, both are required
            if (width > 0 and height <= 0) or (height > 0 and width <= 0):
                raise forms.ValidationError(
                    "Please enter both Width and Height."
                )

            return cleaned_data

    def clean_quantity(self):

        quantity = self.cleaned_data.get('quantity')

        if quantity <= 0:
            raise forms.ValidationError(
                "Quantity must be greater than zero."
            )

        return quantity

    def clean_unit_price(self):

        unit_price = self.cleaned_data.get('unit_price')

        if unit_price < 0:
            raise forms.ValidationError(
                "Unit price cannot be negative."
            )

        return unit_price