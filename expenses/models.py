from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Company

User = get_user_model()


class ExpenseCategory(models.Model):

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=255)

    code = models.CharField(max_length=50)

    description = models.TextField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('company', 'code')
        ordering = ['name']

    def __str__(self):
        return self.name


class Expense(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('paid', 'Paid'),
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.PROTECT)

    expense_number = models.CharField(max_length=100, unique=True)

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    amount = models.DecimalField(max_digits=18, decimal_places=2)

    expense_date = models.DateField()

    attachment = models.FileField(
        upload_to='expenses/',
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    submitted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='submitted_expenses'
    )

    approved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_expenses'
    )

    approved_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.expense_number