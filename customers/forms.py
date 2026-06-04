from django import forms
from .models import Customer


TAILWIND_INPUT = """
w-full rounded-xl border border-gray-300 bg-white px-4 py-3
text-sm text-gray-700 shadow-sm
focus:border-blue-500 focus:ring-4 focus:ring-blue-100
outline-none transition
"""

TAILWIND_SELECT = """
w-full rounded-xl border border-gray-300 bg-white px-4 py-3
text-sm text-gray-700 shadow-sm
focus:border-blue-500 focus:ring-4 focus:ring-blue-100
outline-none transition
"""

TAILWIND_TEXTAREA = """
w-full rounded-xl border border-gray-300 bg-white px-4 py-3
text-sm text-gray-700 shadow-sm resize-none
focus:border-blue-500 focus:ring-4 focus:ring-blue-100
outline-none transition
"""

TAILWIND_CHECKBOX = """
h-5 w-5 rounded border-gray-300 text-blue-600
focus:ring-blue-500
"""


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer

        fields = [
            'customer_type',
            'full_name',
            'company_name',
            'phone',
            'alternative_phone',
            'email',
            
            'address',
            'country',
            'region',
            
            'is_active',
            
        ]

        widgets = {

            'customer_type': forms.Select(attrs={
                'class': TAILWIND_SELECT
            }),

            'full_name': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Enter full name'
            }),

            'company_name': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Enter company name'
            }),

            'phone': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Enter phone number'
            }),

            'alternative_phone': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Enter alternative phone'
            }),

            'email': forms.EmailInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Enter email address'
            }),

            

            'address': forms.Textarea(attrs={
                'class': TAILWIND_TEXTAREA,
                'rows': 3,
                'placeholder': 'Enter full address'
            }),

            'country': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Country'
            }),

            'region': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Region'
            }),

            
            'is_active': forms.CheckboxInput(attrs={
                'class': TAILWIND_CHECKBOX
            }),

            
        }

    def clean(self):

        cleaned_data = super().clean()

        customer_type = cleaned_data.get('customer_type')
        company_name = cleaned_data.get('company_name')

        if customer_type == 'company' and not company_name:

            self.add_error(
                'company_name',
                'Company name is required.'
            )

        return cleaned_data
    



from django import forms
from .models import Supplier


TAILWIND_INPUT = """
w-full rounded-xl border border-gray-300 bg-white px-4 py-3
text-sm text-gray-700
focus:border-gray-400 focus:ring-4 focus:ring-gray-100
outline-none transition
"""

TAILWIND_TEXTAREA = """
w-full rounded-xl border border-gray-300 bg-white px-4 py-3
text-sm text-gray-700 resize-none
focus:border-gray-400 focus:ring-4 focus:ring-gray-100
outline-none transition
"""

TAILWIND_CHECKBOX = """
h-5 w-5 rounded border-gray-300 text-green-600
focus:ring-green-500
"""


class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier

        fields = [
            'company_name',
            'contact_person',
            'phone',
            'alternative_phone',
            'email',
            'tin_number',
            'vrn_number',
            'address',
            'country',
            'region',
            'district',
            'city',
            'website',
            'bank_name',
            'bank_account_number',
            'is_active',
            'notes',
        ]

        widgets = {

            'company_name': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Company name'
            }),

            'contact_person': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Contact person'
            }),

            'phone': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Phone number'
            }),

            'alternative_phone': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Alternative phone'
            }),

            'email': forms.EmailInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Email address'
            }),

            'tin_number': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'TIN number'
            }),

            'vrn_number': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'VRN number'
            }),

            'address': forms.Textarea(attrs={
                'class': TAILWIND_TEXTAREA,
                'rows': 3,
                'placeholder': 'Address'
            }),

            'country': forms.TextInput(attrs={
                'class': TAILWIND_INPUT
            }),

            'region': forms.TextInput(attrs={
                'class': TAILWIND_INPUT
            }),

            'district': forms.TextInput(attrs={
                'class': TAILWIND_INPUT
            }),

            'city': forms.TextInput(attrs={
                'class': TAILWIND_INPUT
            }),

            'website': forms.URLInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Website URL'
            }),

            'bank_name': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Bank name'
            }),

            'bank_account_number': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Account number'
            }),

            'is_active': forms.CheckboxInput(attrs={
                'class': TAILWIND_CHECKBOX
            }),

            'notes': forms.Textarea(attrs={
                'class': TAILWIND_TEXTAREA,
                'rows': 4,
                'placeholder': 'Additional notes'
            }),

        }