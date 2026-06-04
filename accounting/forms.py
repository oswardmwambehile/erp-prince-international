from django import forms
from django.forms import modelformset_factory
from .models import JournalEntry, JournalEntryLine, ChartOfAccount
from .utils import get_default_company


# =========================
# TAILWIND STYLES
# =========================
TAILWIND_INPUT = "w-full rounded-lg border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
TAILWIND_SELECT = "w-full rounded-lg border border-gray-300 px-3 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-blue-500"
TAILWIND_TEXTAREA = "w-full rounded-lg border border-gray-300 px-3 py-2 h-24 focus:outline-none focus:ring-2 focus:ring-blue-500"


# =========================
# JOURNAL ENTRY FORM (HEADER)
# =========================
class JournalEntryForm(forms.ModelForm):

    class Meta:
        model = JournalEntry
        fields = [
            
            'reference',
            'description',
            'posting_date',
            'status'
        ]

        widgets = {
            

            'reference': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Reference (optional)'
            }),

            'description': forms.Textarea(attrs={
                'class': TAILWIND_TEXTAREA,
                'placeholder': 'Enter journal description'
            }),

            'posting_date': forms.DateInput(attrs={
                'type': 'date',
                'class': TAILWIND_INPUT
            }),

            'status': forms.Select(attrs={
                'class': TAILWIND_SELECT
            }),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)

        # FORCE DEFAULT COMPANY (ERP SAFETY)
        if not instance.company_id:
            instance.company = get_default_company()

        if commit:
            instance.save()

        return instance


# =========================
# JOURNAL LINE FORM
# =========================
class JournalEntryLineForm(forms.ModelForm):

    class Meta:
        model = JournalEntryLine
        fields = [
            'account',
            'description',
            'debit',
            'credit'
        ]

        widgets = {
            'account': forms.Select(attrs={
                'class': TAILWIND_SELECT
            }),

            'description': forms.TextInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': 'Line description'
            }),

            'debit': forms.NumberInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': '0.00',
                'min': 0
            }),

            'credit': forms.NumberInput(attrs={
                'class': TAILWIND_INPUT,
                'placeholder': '0.00',
                'min': 0
            }),
        }

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company', None)
        super().__init__(*args, **kwargs)

        # 🔥 FILTER ACCOUNTS BY COMPANY (VERY IMPORTANT ERP FIX)
        if company:
            self.fields['account'].queryset = ChartOfAccount.objects.filter(
                company=company,
                is_active=True
            )


# =========================
# JOURNAL LINE FORMSET
# =========================
JournalEntryLineFormSet = modelformset_factory(
    JournalEntryLine,
    form=JournalEntryLineForm,
    extra=2,
    can_delete=True
)


from django import forms
from .models import AccountType


class AccountTypeForm(forms.ModelForm):
    class Meta:
        model = AccountType
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter account type name'
            }),
        }

from django import forms
from .models import ChartOfAccount


class ChartOfAccountForm(forms.ModelForm):

    class Meta:
        model = ChartOfAccount
        fields = [
            "account_type",
            "account_code",
            "account_name",
            "parent_account",
            "opening_balance",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "w-full border rounded-xl px-3 py-2 focus:ring-2 focus:ring-green-500"
            })