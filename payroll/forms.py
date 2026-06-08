from django import forms
from .models import Employee, Payroll


# =========================
# EMPLOYEE FORM
# =========================
class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = [
            "user",
            "employee_id",
            "salary",
            "hire_date",
            "employment_status",
        ]

        widgets = {
            "hire_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        base_class = (
            "w-full px-4 py-3 border border-gray-300 "
            "rounded-xl focus:ring-2 focus:ring-green-500 "
            "focus:border-green-500 focus:outline-none"
        )

        for field in self.fields.values():
            field.widget.attrs["class"] = base_class

        self.fields["user"].label_from_instance = (
            lambda obj: f"{obj.first_name} {obj.last_name}".strip()
            if obj.first_name or obj.last_name
            else obj.email
        )


# =========================
# PAYROLL FORM
# =========================
class PayrollForm(forms.ModelForm):

    MONTH_CHOICES = [
        (1, "January"),
        (2, "February"),
        (3, "March"),
        (4, "April"),
        (5, "May"),
        (6, "June"),
        (7, "July"),
        (8, "August"),
        (9, "September"),
        (10, "October"),
        (11, "November"),
        (12, "December"),
    ]

    payroll_month = forms.ChoiceField(
        choices=MONTH_CHOICES
    )

    class Meta:
        model = Payroll

        fields = [
            "employee",
            "allowance",
            "deduction",
            "tax",
            "payroll_month",
            "payroll_year",
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

        self.fields["allowance"].widget.attrs["placeholder"] = "Enter allowance"
        self.fields["deduction"].widget.attrs["placeholder"] = "Enter deduction"
        self.fields["tax"].widget.attrs["placeholder"] = "Enter tax amount"
        self.fields["payroll_year"].widget.attrs["placeholder"] = "2026"

        self.fields["employee"].label_from_instance = (
            lambda obj: (
                f"{obj.user.first_name} {obj.user.last_name} "
                f"({obj.employee_id})"
            )
        )

    def clean(self):

        cleaned_data = super().clean()

        employee = cleaned_data.get("employee")
        month = cleaned_data.get("payroll_month")
        year = cleaned_data.get("payroll_year")

        payrolls = Payroll.objects.filter(
            employee=employee,
            payroll_month=month,
            payroll_year=year,
        )

        # Ignore current payroll during edit
        if self.instance.pk:
            payrolls = payrolls.exclude(pk=self.instance.pk)

        if payrolls.exists():
            raise forms.ValidationError(
                "Payroll already exists for this employee in the selected month."
            )

        return cleaned_data