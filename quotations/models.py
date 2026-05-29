from decimal import Decimal, ROUND_HALF_UP
from django.db import models
from django.utils import timezone

from customers.models import Customer
from accounts.models import User
from inventory.models import Product


# =====================================================
# QUOTATION MODEL
# =====================================================
class Quotation(models.Model):

    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Sent', 'Sent'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    PAYMENT_MODE = (
        ('Normal', 'Normal'),
        ('Fast Track', 'Fast Track'),
        ('China Order', 'China Order'),
    )

    quotation_no = models.CharField(
        max_length=100,
        unique=True,
        blank=True
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='quotations'
    )

    project_name = models.CharField(
        max_length=255,
        blank=True
    )

    project_location = models.CharField(
        max_length=255,
        blank=True
    )

    contact_person = models.CharField(
        max_length=255,
        blank=True
    )

    quotation_date = models.DateField()

    # =========================
    # PAYMENT MODE
    

    # ========================= 
    # VAT
    # =========================
    vat_included = models.BooleanField(
        default=False
    )

    vat_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal('18.00')
    )

    # =========================
    # TOTALS
    # =========================
    subtotal = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=Decimal('0.00')
    )

    discount_amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=Decimal('0.00')
    )

    tax_amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=Decimal('0.00')
    )

    grand_total = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=Decimal('0.00')
    )

    # =========================
    # STATUS
    # =========================
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Draft'
    )

    # =========================
    # USERS
    # =========================
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='quotations_created'
    )

    sales_person = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sales_quotations'
    )

    # =========================
    # TIMESTAMPS
    # =========================
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    # =====================================================
    # AUTO QUOTATION NUMBER
    # =====================================================
    def save(self, *args, **kwargs):

        if not self.quotation_no:

            year = timezone.now().year

            last = Quotation.objects.order_by('id').last()

            number = (last.id + 1) if last else 1

            self.quotation_no = f"QT-{year}-{number:04d}"

        super().save(*args, **kwargs)

    # =====================================================
    # CALCULATE TOTALS
    # =====================================================
    def calculate_totals(self):

        items = self.items.all()

        subtotal = sum(
            (item.total_price or Decimal('0.00'))
            for item in items
        )

        self.subtotal = subtotal

        # VAT CALCULATION
        if self.vat_included is True:

            vat_rate = (
                self.vat_percentage /
                Decimal('100')
            )

            self.tax_amount = (
                subtotal * vat_rate
            )

        else:
            self.tax_amount = Decimal('0.00')

        # GRAND TOTAL
        self.grand_total = (
            self.subtotal
            + self.tax_amount
            - self.discount_amount
        )

        self.save(update_fields=[
            'subtotal',
            'tax_amount',
            'grand_total'
        ])

    def __str__(self):
        return self.quotation_no


# =====================================================
# QUOTATION ITEM MODEL
# =====================================================
class QuotationItem(models.Model):

    quotation = models.ForeignKey(
        Quotation,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    # =========================
    # ITEM DETAILS
    # =========================
    item_code = models.CharField(
        max_length=100,
        blank=True
    )

   

    aluminium_profile = models.CharField(
        max_length=255,
        blank=True
    )

    glass = models.CharField(
        max_length=255,
        blank=True
    )

    # =========================
    # DISPLAY ONLY
    # NOT USED IN CALCULATION
    # =========================
    width = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00')
    )

    height = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00')
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    # =========================
    # USER ENTERS SQM
    # =========================
    sqm = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00')
    )

    total_sqm = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00')
    )

    # =========================
    # PRICING
    # =========================
    unit_price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=Decimal('0.00')
    )

    total_price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=Decimal('0.00')
    )

    cts = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # =====================================================
    # ROUNDING LOGIC
    # =====================================================
    def round_total_sqm(self, value):

        value = Decimal(value)

        integer_part = int(value)

        decimal_part = value - Decimal(integer_part)

        # 3.5 -> 4
        # 3.6 -> 4
        # 3.9 -> 4
        if decimal_part >= Decimal('0.5'):

            return Decimal(integer_part + 1)

        # 3.4 -> 3.4
        return value.quantize(
            Decimal('0.1'),
            rounding=ROUND_HALF_UP
        )

    def save(self, *args, **kwargs):

        width = Decimal(self.width or 0)

        height = Decimal(self.height or 0)

        qty = Decimal(self.quantity or 0)

        unit_price = Decimal(self.unit_price or 0)

        # =========================================
        # SQM
        # width * height / 1000000
        # =========================================
        self.sqm = (
            (width * height) / Decimal('1000000')
        ).quantize(
            Decimal('0.1'),
            rounding=ROUND_HALF_UP
        )

        # =========================================
        # TOTAL SQM
        # sqm * quantity
        # ONLY THIS GETS SPECIAL ROUNDING
        # =========================================
        raw_total_sqm = self.sqm * qty

        self.total_sqm = self.round_total_sqm(
            raw_total_sqm
        )

        # =========================================
        # TOTAL PRICE
        # NO ROUNDING LOGIC HERE
        # =========================================
        self.total_price = (
            self.total_sqm * unit_price
        ).quantize(
            Decimal('0.01'),
            rounding=ROUND_HALF_UP
        )

        super().save(*args, **kwargs)

        # =========================================
        # UPDATE QUOTATION TOTALS
        # =========================================
        if self.quotation_id:
            self.quotation.calculate_totals()