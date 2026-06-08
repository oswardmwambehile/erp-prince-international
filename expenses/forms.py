from django import forms

from accounts.models import Company
from .models import ExpenseCategory, Expense


# =========================================
# EXPENSE CATEGORY FORM
# =========================================
class ExpenseCategoryForm(forms.ModelForm):

    class Meta:
        model = ExpenseCategory

        fields = [
            'company',
            'name',
            'code',
            'description',
            'is_active'
        ]

        widgets = {

            # COMPANY DROPDOWN
            'company': forms.Select(attrs={
                'class': 'w-full rounded-xl border border-gray-300 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-green-500 bg-white'
            }),

            'name': forms.TextInput(attrs={
                'class': 'w-full rounded-xl border border-gray-300 px-4 py-3',
                'placeholder': 'Category name'
            }),

            'code': forms.TextInput(attrs={
                'class': 'w-full rounded-xl border border-gray-300 px-4 py-3',
                'placeholder': 'Category code'
            }),

            'description': forms.Textarea(attrs={
                'class': 'w-full rounded-xl border border-gray-300 px-4 py-3',
                'rows': 4,
                'placeholder': 'Description'
            }),

            'is_active': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-green-600 rounded'
            }),
        }

    def __init__(self, *args, **kwargs):

        # REMOVE COMPANY ARGUMENT
        company = kwargs.pop('company', None)

        super().__init__(*args, **kwargs)

        # LOAD ALL COMPANIES
        self.fields[
            'company'
        ].queryset = Company.objects.all()

        # OPTIONAL PRESELECT
        if company:

            self.fields[
                'company'
            ].initial = company

    def clean_code(self):

        code = self.cleaned_data.get('code')

        if code:
            return code.upper()

        return code


# =========================================
# EXPENSE FORM
# =========================================
class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense

        fields = [
            'category',
            'title',
            'branch',
            'description',
            'amount',
            'expense_date',
            'attachment',
        ]

        widgets = {

            'category': forms.Select(attrs={
                'class': 'w-full rounded-xl border border-gray-300 px-4 py-3'
            }),

            'title': forms.TextInput(attrs={
                'class': 'w-full rounded-xl border border-gray-300 px-4 py-3',
                'placeholder': 'Expense title'
            }),
            'branch': forms.Select(attrs={
                'class': 'w-full rounded-xl border border-gray-300 px-4 py-3',
                'placeholder': 'Select Branch'
            }),


            'description': forms.Textarea(attrs={
                'class': 'w-full rounded-xl border border-gray-300 px-4 py-3',
                'rows': 4,
                'placeholder': 'Expense description'
            }),

            'amount': forms.NumberInput(attrs={
                'class': 'w-full rounded-xl border border-gray-300 px-4 py-3',
                'placeholder': '0.00',
                'step': '0.01'
            }),

            'expense_date': forms.DateInput(attrs={
                'class': 'w-full rounded-xl border border-gray-300 px-4 py-3',
                'type': 'date'
            }),

            'attachment': forms.ClearableFileInput(attrs={
                'class': 'w-full rounded-xl border border-gray-300 px-4 py-3'
            }),
        }

    def __init__(self, *args, **kwargs):

        # REMOVE CUSTOM COMPANY ARGUMENT
        company = kwargs.pop('company', None)

        super().__init__(*args, **kwargs)

        # FILTER CATEGORY BY COMPANY
        if company:

            self.fields[
                'category'
            ].queryset = ExpenseCategory.objects.filter(
                company=company,
                is_active=True
            )

    def clean_amount(self):

        amount = self.cleaned_data.get('amount')

        if amount is None or amount <= 0:

            raise forms.ValidationError(
                'Amount must be greater than zero.'
            )

        return amount