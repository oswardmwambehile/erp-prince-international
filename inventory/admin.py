from django.contrib import admin
from .models import (
    Category,
    Unit,
    Warehouse,
    Product,
    Stock,
    StockMovement
)


# =========================
# CATEGORY ADMIN
# =========================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


# =========================
# UNIT ADMIN
# =========================
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'symbol')
    search_fields = ('name', 'symbol')
    ordering = ('name',)


# =========================
# WAREHOUSE ADMIN
# =========================
@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'manager')
    search_fields = ('name', 'location')
    list_filter = ('location',)
    autocomplete_fields = ('manager',)


# =========================
# STOCK INLINE (FOR PRODUCT)
# =========================
class StockInline(admin.TabularInline):
    model = Stock
    extra = 0
    autocomplete_fields = ('warehouse',)
    readonly_fields = ('last_updated',)


# =========================
# PRODUCT ADMIN (MAIN FOCUS)
# =========================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'product_code',
        'name',
        'category',
        'unit',
        'buying_price',
        'selling_price',
        'minimum_stock',
        'created_at',
    )

    list_filter = (
        'category',
        'unit',
        'created_at',
    )

    search_fields = (
        'name',
        'product_code',
        'barcode',
    )

    ordering = ('-created_at',)

    inlines = [StockInline]

    fieldsets = (
        ('Basic Information', {
            'fields': (
                'product_code',
                'name',
                'description',
                'category',
                'unit',
            )
        }),

        ('Pricing', {
            'fields': (
                'buying_price',
                'selling_price',
            )
        }),

        ('Stock Settings', {
            'fields': (
                'minimum_stock',
                'barcode',
            )
        }),
    )


# =========================
# STOCK ADMIN
# =========================
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):

    list_display = (
        'product',
        'warehouse',
        'quantity',
        'last_updated',
    )

    list_filter = ('warehouse', 'product')
    search_fields = ('product__name',)

    autocomplete_fields = ('product', 'warehouse')


# =========================
# STOCK MOVEMENT ADMIN
# =========================
@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):

    list_display = (
        'product',
        'warehouse',
        'movement_type',
        'quantity',
        'balance_after',
        'created_by',
        'created_at',
    )

    list_filter = (
        'movement_type',
        'warehouse',
        'created_at',
    )

    search_fields = (
        'product__name',
        'reference_type',
    )

    readonly_fields = (
        'balance_after',
        'created_at',
    )

    autocomplete_fields = (
        'product',
        'warehouse',
        'created_by',
    )