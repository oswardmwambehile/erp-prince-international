from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Company

User = get_user_model()


class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('terminated', 'Terminated'),
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    employee_id = models.CharField(max_length=100, unique=True)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    email = models.EmailField()
    phone = models.CharField(max_length=50)

    salary = models.DecimalField(max_digits=18, decimal_places=2)

    hire_date = models.DateField()

    employment_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Payroll(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('processed', 'Processed'),
        ('paid', 'Paid'),
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    payroll_number = models.CharField(max_length=100, unique=True)

    basic_salary = models.DecimalField(max_digits=18, decimal_places=2)

    allowance = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    deduction = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    tax = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    net_salary = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )

    payroll_month = models.IntegerField()
    payroll_year = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    processed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    processed_at = models.DateTimeField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.payroll_number