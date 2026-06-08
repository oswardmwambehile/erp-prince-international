from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Department, Company

User = get_user_model()


from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Employee(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('terminated', 'Terminated'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    employee_id = models.CharField(
        max_length=100,
        unique=True
    )

    salary = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )

    hire_date = models.DateField()

    employment_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_full_name()


class Payroll(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('processed', 'Processed'),
        ('paid', 'Paid'),
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    payroll_number = models.CharField(max_length=100, unique=True)

    basic_salary = models.DecimalField(max_digits=18, decimal_places=2)
    allowance = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    deduction = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    net_salary = models.DecimalField(max_digits=18, decimal_places=2, blank=True)

    payroll_month = models.IntegerField()
    payroll_year = models.IntegerField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    processed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    processed_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.net_salary = self.basic_salary + self.allowance - self.deduction - self.tax
        super().save(*args, **kwargs)

    def __str__(self):
        return self.payroll_number

