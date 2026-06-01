from django.db import models
from django.core.exceptions import ValidationError
from accounts.models import Company


# =====================================================
# UTILITY: DEFAULT COMPANY
# =====================================================
def get_default_company():
    company, _ = Company.objects.get_or_create(
        name="Prince International"
    )
    return company


# =====================================================
# ACCOUNT TYPE
# =====================================================
class AccountType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# =====================================================
# CHART OF ACCOUNTS
# =====================================================
class ChartOfAccount(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    account_type = models.ForeignKey(
        AccountType,
        on_delete=models.PROTECT
    )

    account_code = models.CharField(max_length=50)
    account_name = models.CharField(max_length=255)

    parent_account = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children"
    )

    opening_balance = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('company', 'account_code')
        ordering = ['account_code']

    def __str__(self):
        return f"{self.account_code} - {self.account_name} - ({self.account_type})"

    def save(self, *args, **kwargs):
        if not self.company_id:
            self.company = get_default_company()
        super().save(*args, **kwargs)


# =====================================================
# JOURNAL ENTRY (HEADER)
# =====================================================
class JournalEntry(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('posted', 'Posted'),
        ('cancelled', 'Cancelled'),
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    journal_number = models.CharField(max_length=100)

    reference = models.CharField(max_length=255, blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    posting_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('company', 'journal_number')
        ordering = ['-created_at']

    def __str__(self):
        return self.journal_number

    def save(self, *args, **kwargs):
        if not self.company_id:
            self.company = get_default_company()
        super().save(*args, **kwargs)

    # =================================================
    # ERP RULE: CHECK BALANCE
    # =================================================
    def is_balanced(self):
        debit = sum(line.debit for line in self.lines.all())
        credit = sum(line.credit for line in self.lines.all())
        return debit == credit


# =====================================================
# JOURNAL ENTRY LINES (DEBIT / CREDIT)
# =====================================================
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

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.account.account_name}"

    # =================================================
    # ERP VALIDATION RULES
    # =================================================
    def clean(self):

        # Cannot have both debit and credit
        if self.debit > 0 and self.credit > 0:
            raise ValidationError(
                "A line cannot have both debit and credit"
            )

        # Must have at least one
        if self.debit == 0 and self.credit == 0:
            raise ValidationError(
                "A line must have either debit or credit"
            )