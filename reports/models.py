from django.db import models
from decimal import Decimal
from customers.models import Customer
from inventory.models import Product


class QuotationNormal(models.Model):
    quotation_no = models.CharField(max_length=30, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quotation_date = models.DateField(auto_now_add=True)

    def total_amount(self):
        return sum(item.total_price for item in self.items.all())

    def __str__(self):
        return self.quotation_no


class QuotationItemNormal(models.Model):
    quotation = models.ForeignKey(
         QuotationNormal,
        related_name="items",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
   
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    total_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        editable=False,
        default=0
    )

    def save(self, *args, **kwargs):
        self.total_price = Decimal(self.quantity) * Decimal(self.unit_price)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name