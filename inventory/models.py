from django.db import models
from accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE
    )

    product_code = models.CharField(max_length=100, unique=True)

    name = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    buying_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    selling_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    minimum_stock = models.IntegerField(default=0)

    barcode = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(default=0)

    last_updated = models.DateTimeField(auto_now=True)


class StockMovement(models.Model):

    MOVEMENT_TYPES = (
        ('IN', 'IN'),
        ('OUT', 'OUT'),
        ('ADJUSTMENT', 'ADJUSTMENT'),
        ('TRANSFER', 'TRANSFER'),
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE
    )

    movement_type = models.CharField(
        max_length=20,
        choices=MOVEMENT_TYPES
    )

    reference_type = models.CharField(max_length=100)

    reference_id = models.IntegerField(null=True, blank=True)

    quantity = models.IntegerField()

    balance_after = models.IntegerField()

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    note = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)