from django.db import models
from accounts.models import Company


class AccountType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ChartOfAccount(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    account_type = models.ForeignKey(
        AccountType,
        on_delete=models.PROTECT
    )

    account_code = models.CharField(
        max_length=50,
        unique=True
    )

    account_name = models.CharField(max_length=255)

    parent_account = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    opening_balance = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_code} - {self.account_name}"


class JournalEntry(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('posted', 'Posted'),
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    journal_number = models.CharField(
        max_length=100,
        unique=True
    )

    reference = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    posting_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.journal_number


class JournalEntryLine(models.Model):
    journal_entry = models.ForeignKey(
        JournalEntry,
        on_delete=models.CASCADE,
        related_name='lines'
    )

    account = models.ForeignKey(
        ChartOfAccount,
        on_delete=models.PROTECT
    )

    description = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    debit = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    credit = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return str(self.journal_entry)