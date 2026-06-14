from django import forms
from django.contrib.auth import get_user_model

from accounts.models import Company, Branch
from .models import ExpenseCategory, Expense

User = get_user_model()


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

        company = kwargs.pop('company', None)

        super().__init__(*args, **kwargs)

        self.fields['company'].queryset = Company.objects.all()

        if company:
            self.fields['company'].initial = company

    def clean_code(self):

        code = self.cleaned_data.get('code')

        if code:
            return code.upper()

        return code



from django import forms
from django.contrib.auth import get_user_model

from accounts.models import Company, Branch
from .models import ExpenseCategory, Expense

User = get_user_model()


# =========================================
# EXPENSE FORM
# =========================================
class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense

        fields = [
            "category",
            "employee",
            "branch",
            "title",
            "description",
            "amount",
            "paid_amount",
            "remaining_balance",
            "expense_date",
            "attachment",
        ]

        widgets = {

            "category": forms.Select(attrs={
                "class": "w-full rounded-xl border border-gray-300 px-4 py-3"
            }),

            "employee": forms.Select(attrs={
                "class": "w-full rounded-xl border border-gray-300 px-4 py-3"
            }),

            "branch": forms.Select(attrs={
                "class": "w-full rounded-xl border border-gray-300 px-4 py-3"
            }),

            "title": forms.TextInput(attrs={
                "class": "w-full rounded-xl border border-gray-300 px-4 py-3",
                "placeholder": "Expense title"
            }),

            "description": forms.Textarea(attrs={
                "class": "w-full rounded-xl border border-gray-300 px-4 py-3",
                "rows": 4,
                "placeholder": "Expense description"
            }),

            "amount": forms.NumberInput(attrs={
                "class": "w-full rounded-xl border border-gray-300 px-4 py-3",
                "placeholder": "Amount",
                "step": "0.01"
            }),

            "paid_amount": forms.NumberInput(attrs={
                "class": "w-full rounded-xl border border-gray-300 px-4 py-3",
                "placeholder": "Today's Payment",
                "step": "0.01"
            }),

            "remaining_balance": forms.NumberInput(attrs={
                "class": "w-full rounded-xl border border-gray-300 px-4 py-3",
                "readonly": "readonly",
                "placeholder": "Remaining Balance"
            }),

            "expense_date": forms.DateInput(attrs={
                "class": "w-full rounded-xl border border-gray-300 px-4 py-3",
                "type": "date"
            }),

            "attachment": forms.ClearableFileInput(attrs={
                "class": "w-full rounded-xl border border-gray-300 px-4 py-3"
            }),
        }

    def __init__(self, *args, **kwargs):

        company = kwargs.pop("company", None)

        super().__init__(*args, **kwargs)

        if company:

            self.fields["category"].queryset = (
                ExpenseCategory.objects.filter(
                    company=company,
                    is_active=True
                )
            )

            self.fields["branch"].queryset = (
                Branch.objects.filter(
                    company=company
                )
            )

        self.fields["employee"].queryset = (
            User.objects.filter(
                is_active=True
            )
        )

        self.fields["employee"].label_from_instance = (
            lambda obj:
            f"{obj.first_name} {obj.last_name}".strip()
            or obj.email
        )

        self.fields["employee"].required = False
        self.fields["paid_amount"].required = False
        self.fields["remaining_balance"].required = False

        # IMPORTANT:
        # When updating, the user enters ONLY
        # today's payment, not the accumulated one.
        if self.instance and self.instance.pk:
            self.fields["paid_amount"].initial = 0

    def clean_amount(self):

        amount = self.cleaned_data.get("amount")

        if amount is None or amount <= 0:
            raise forms.ValidationError(
                "Amount must be greater than zero."
            )

        return amount

    def clean(self):

        cleaned_data = super().clean()

        category = cleaned_data.get("category")
        employee = cleaned_data.get("employee")

        amount = cleaned_data.get("amount") or 0
        payment = cleaned_data.get("paid_amount") or 0

        if category:

            category_name = (
                category.name.strip().lower()
            )

            # =====================================
            # ADVANCE SALARY
            # =====================================
            if category_name == "advance salary":

                if not employee:
                    self.add_error(
                        "employee",
                        "Please select an employee."
                    )

                if payment < 0:
                    self.add_error(
                        "paid_amount",
                        "Payment cannot be negative."
                    )

                # The view calculates the final balance
                cleaned_data["remaining_balance"] = amount

            # =====================================
            # COMMISSION
            # =====================================
            elif category_name == "commission":

                if not employee:
                    self.add_error(
                        "employee",
                        "Please select an employee."
                    )

                cleaned_data["remaining_balance"] = 0

            # =====================================
            # OTHER CATEGORIES
            # =====================================
            else:

                cleaned_data["paid_amount"] = 0
                cleaned_data["remaining_balance"] = 0

        return cleaned_data

from django import forms
from .models import DailyCashBalance


class DailyCashBalanceForm(forms.ModelForm):
    class Meta:
        model = DailyCashBalance
        fields = [
            "company",
            "date",
            "opening_balance",
        ]

        widgets = {
            "company": forms.Select(
                attrs={
                    "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
                }
            ),
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
                }
            ),
            "opening_balance": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "placeholder": "Enter Opening Balance",
                    "class": "w-full rounded-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500",
                }
            ),
        }

        labels = {
            "company": "Company",
            "date": "Date",
            "opening_balance": "Opening Balance (TZS)",
        }