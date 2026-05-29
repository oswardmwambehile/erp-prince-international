from django import forms
from .models import Company, Branch,Department,Position


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company

        fields = [
            'name',
            'code',
            'email',
            'phone',
            'address',
            'is_active'
        ]

        widgets = {

            # COMPANY NAME
            'name': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-700 placeholder-gray-400 focus:border-blue-500 focus:ring-2 focus:ring-blue-100 outline-none transition',
                'placeholder': 'Enter company name'
            }),

            # CODE
            'code': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-700 placeholder-gray-400 focus:border-blue-500 focus:ring-2 focus:ring-blue-100 outline-none transition',
                'placeholder': 'Enter company code'
            }),

            # EMAIL
            'email': forms.EmailInput(attrs={
                'class': 'w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-700 placeholder-gray-400 focus:border-blue-500 focus:ring-2 focus:ring-blue-100 outline-none transition',
                'placeholder': 'company@example.com'
            }),

            # PHONE
            'phone': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-700 placeholder-gray-400 focus:border-blue-500 focus:ring-2 focus:ring-blue-100 outline-none transition',
                'placeholder': '+255712345678'
            }),

            # ADDRESS
            'address': forms.Textarea(attrs={
                'class': 'w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-700 placeholder-gray-400 focus:border-blue-500 focus:ring-2 focus:ring-blue-100 outline-none transition resize-none',
                'rows': 4,
                'placeholder': 'Enter company address'
            }),

            # ACTIVE
            'is_active': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500'
            }),
        }





class BranchForm(forms.ModelForm):

    class Meta:
        model = Branch

        fields = [
            'company',
            'name',
            'code',
            'location',
            'is_active'
        ]

        widgets = {

            # COMPANY
            'company': forms.Select(attrs={
                'class': 'w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-700 focus:border-blue-500 focus:ring-2 focus:ring-blue-100 outline-none transition'
            }),

            # NAME
            'name': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-700 placeholder-gray-400 focus:border-blue-500 focus:ring-2 focus:ring-blue-100 outline-none transition',
                'placeholder': 'Enter branch name'
            }),

            # CODE
            'code': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-700 placeholder-gray-400 focus:border-blue-500 focus:ring-2 focus:ring-blue-100 outline-none transition',
                'placeholder': 'Enter branch code'
            }),

            # LOCATION
            'location': forms.TextInput(attrs={
                'class': 'w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-700 placeholder-gray-400 focus:border-blue-500 focus:ring-2 focus:ring-blue-100 outline-none transition',
                'placeholder': 'Enter location'
            }),

            # ACTIVE
            'is_active': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500'
            }),
        }







class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department

        fields = [
            'company',
            'name',
            'code',
            'is_active'
        ]

        widgets = {

            # COMPANY
            'company': forms.Select(attrs={
                'class': 'w-full rounded-xl border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-700 focus:ring-2 focus:ring-blue-500 focus:outline-none'
            }),

            # NAME
            'name': forms.TextInput(attrs={
                'class': 'w-full rounded-xl border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-700 focus:ring-2 focus:ring-blue-500 focus:outline-none',
                'placeholder': 'Enter department name'
            }),

            # CODE
            'code': forms.TextInput(attrs={
                'class': 'w-full rounded-xl border border-gray-300 bg-white px-4 py-2.5 text-sm text-gray-700 focus:ring-2 focus:ring-blue-500 focus:outline-none',
                'placeholder': 'Enter department code'
            }),

            # STATUS
            'is_active': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500'
            }),
        }




class PositionForm(forms.ModelForm):

    class Meta:
        model = Position

        fields = [
            'company',
            'name',
            'description',
            'is_active'
        ]

        widgets = {

            # COMPANY
            'company': forms.Select(attrs={
                'class': 'w-full rounded-xl border border-gray-300 bg-white px-4 py-2.5 text-sm focus:ring-2 focus:ring-blue-500 focus:outline-none'
            }),

            # NAME
            'name': forms.TextInput(attrs={
                'class': 'w-full rounded-xl border border-gray-300 px-4 py-2.5 text-sm focus:ring-2 focus:ring-blue-500 focus:outline-none',
                'placeholder': 'Enter position name'
            }),

            # DESCRIPTION
            'description': forms.Textarea(attrs={
                'class': 'w-full rounded-xl border border-gray-300 px-4 py-2.5 text-sm focus:ring-2 focus:ring-blue-500 focus:outline-none',
                'rows': 4,
                'placeholder': 'Enter description'
            }),

            # ACTIVE
            'is_active': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-blue-600 border-gray-300 rounded'
            }),
        }


from django import forms
from .models import User
import re


class UserForm(forms.ModelForm):

    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'w-full h-10 px-3 border border-gray-300 rounded-lg',
            'placeholder': 'Enter password'
        })
    )

    confirm_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'w-full h-10 px-3 border border-gray-300 rounded-lg',
            'placeholder': 'Confirm password'
        })
    )

    class Meta:
        model = User
        fields = [
            'company',
            'branch',
            'department',
            'position',
            'first_name',
            'last_name',
            'email',
            'contact',
           
            'is_staff'
        ]

        widgets = {
            'company': forms.Select(attrs={'class': 'w-full h-10 px-3 border border-gray-300 rounded-lg'}),
            'branch': forms.Select(attrs={'class': 'w-full h-10 px-3 border border-gray-300 rounded-lg'}),
            'department': forms.Select(attrs={'class': 'w-full h-10 px-3 border border-gray-300 rounded-lg'}),
            'position': forms.Select(attrs={'class': 'w-full h-10 px-3 border border-gray-300 rounded-lg'}),

            'first_name': forms.TextInput(attrs={'class': 'w-full h-10 px-3 border border-gray-300 rounded-lg'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full h-10 px-3 border border-gray-300 rounded-lg'}),
            'email': forms.EmailInput(attrs={'class': 'w-full h-10 px-3 border border-gray-300 rounded-lg'}),
            'contact': forms.TextInput(attrs={'class': 'w-full h-10 px-3 border border-gray-300 rounded-lg'}),
        }

    # -----------------------------
    # EMAIL UNIQUE VALIDATION
    # -----------------------------
    def clean_email(self):
        email = self.cleaned_data.get('email')

        qs = User.objects.filter(email=email)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError("Email already exists.")

        return email

    # -----------------------------
    # TANZANIA PHONE VALIDATION
    # -----------------------------
    def clean_contact(self):
        contact = self.cleaned_data.get('contact')

        if not contact:
            return contact

        pattern = r'^(\+255|0)[0-9]{9}$'

        if not re.match(pattern, contact):
            raise forms.ValidationError(
                "Enter valid Tanzanian number (+255XXXXXXXXX or 0XXXXXXXXX)"
            )

        return contact

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # ONLY VALIDATE PASSWORD WHEN CREATING
        if not self.instance.pk:

            if not password:
                raise forms.ValidationError(
                    "Password is required"
                )

            if password != confirm_password:
                raise forms.ValidationError(
                    "Passwords do not match"
                )

        return cleaned_data