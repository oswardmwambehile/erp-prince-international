from django.db import models
from django.core.exceptions import ValidationError


# =========================
# CUSTOMER MODEL
# =========================
class Customer(models.Model):

    CUSTOMER_TYPE = (
        ('individual', 'Individual'),
        ('company', 'Company'),
    )

    customer_type = models.CharField(
        max_length=20,
        choices=CUSTOMER_TYPE
    )

    # Individual name OR contact person
    full_name = models.CharField(
        max_length=255
    )

    # Required if customer_type = company
    company_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=20
    )

    alternative_phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    tin_number = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    vrn_number = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    country = models.CharField(
        max_length=100,
        default='Tanzania'
    )

    region = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    district = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    ward = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    postal_code = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def clean(self):

        if self.customer_type == 'company' and not self.company_name:
            raise ValidationError({
                'company_name': 'Company name is required.'
            })

    @property
    def customer_code(self):
        return f"CUST-{self.id:04d}" if self.id else "CUST-NEW"

    def __str__(self):

        if self.customer_type == 'company':
            return f"{self.customer_code} - {self.company_name}"

        return f"{self.customer_code} - {self.full_name}"


# =========================
# SUPPLIER MODEL
# =========================
class Supplier(models.Model):

    company_name = models.CharField(
        max_length=255
    )

    contact_person = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=20
    )

    alternative_phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    tin_number = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    vrn_number = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    country = models.CharField(
        max_length=100,
        default='Tanzania'
    )

    region = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    district = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    website = models.URLField(
        blank=True,
        null=True
    )

    bank_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    bank_account_number = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    @property
    def supplier_code(self):
        return f"SUP-{self.id:04d}" if self.id else "SUP-NEW"

    def __str__(self):
        return f"{self.supplier_code} - {self.company_name}"