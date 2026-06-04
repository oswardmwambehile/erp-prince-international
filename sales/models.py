from django.db import models

from customers.models import Customer
from quotations.models import Quotation
from inventory.models import Product
from accounts.models import User


class Invoice(models.Model):

    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Unpaid', 'Unpaid'),
        ('Partial', 'Partial'),
        ('Paid', 'Paid'),
    )

    invoice_no = models.CharField(max_length=100, unique=True)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    quotation = models.ForeignKey(
        Quotation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    invoice_date = models.DateField()

    due_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    tax_amount = models.DecimalField(max_digits=12, decimal_places=2)

    discount_amount = models.DecimalField(max_digits=12, decimal_places=2)

    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)


class InvoiceItem(models.Model):

    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    description = models.TextField(blank=True)

    quantity = models.IntegerField()

    unit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    discount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    tax = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    total = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )


class Payment(models.Model):

    PAYMENT_METHODS = (
        ('Cash', 'Cash'),
        ('Bank', 'Bank'),
        ('Mobile', 'Mobile'),
    )

    payment_no = models.CharField(max_length=100, unique=True)

    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE
    )

    payment_date = models.DateField()

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS
    )

    reference_number = models.CharField(
        max_length=255,
        blank=True
    )

    received_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)