from django import forms
from django.core.exceptions import ValidationError

from .models import (
    Category,
    Unit,
    Warehouse,
    Product,
    Stock,
    StockMovement,
)


# =========================================================
# COMMON TAILWIND CLASSES
# =========================================================

INPUT_CLASS = """
w-full
h-12
px-4
rounded-xl
border
border-gray-300
bg-white
focus:ring-2
focus:ring-indigo-500
focus:border-indigo-500
"""


TEXTAREA_CLASS = """
w-full
px-4
py-3
rounded-xl
border
border-gray-300
bg-white
focus:ring-2
focus:ring-indigo-500
focus:border-indigo-500
"""


# =========================================================
# CATEGORY FORM
# =========================================================

class CategoryForm(forms.ModelForm):

    class Meta:

        model = Category

        fields = [
            'name'
        ]

        widgets = {

            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Category name'
            }),

        }


# =========================================================
# UNIT FORM
# =========================================================

class UnitForm(forms.ModelForm):

    class Meta:

        model = Unit

        fields = [
            'name',
            'symbol'
        ]

        widgets = {

            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Unit name'
            }),

            'symbol': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Example: pcs, kg, box'
            }),

        }


# =========================================================
# WAREHOUSE FORM
# =========================================================

class WarehouseForm(forms.ModelForm):

    class Meta:

        model = Warehouse

        fields = [
            'name',
            'location',
            'manager'
        ]

        widgets = {

            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Warehouse name'
            }),

            'location': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Warehouse location'
            }),

            'manager': forms.Select(attrs={
                'class': INPUT_CLASS
            }),

        }


# =========================================================
# PRODUCT FORM
# =========================================================

class ProductForm(forms.ModelForm):

    class Meta:

        model = Product

        fields = [
            'category',
            'unit',
            'product_code',
            'name',
            'description',
            'buying_price',
            'selling_price',
            'minimum_stock',
            'barcode',
        ]

        widgets = {

            'category': forms.Select(attrs={
                'class': INPUT_CLASS,
            }),

            'unit': forms.Select(attrs={
                'class': INPUT_CLASS,
            }),

            'product_code': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Product code',
            }),

            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Product name',
            }),

            'description': forms.Textarea(attrs={
                'class': TEXTAREA_CLASS,
                'rows': 4,
                'placeholder': 'Product description',
            }),

            'buying_price': forms.NumberInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Buying price',
            }),

            'selling_price': forms.NumberInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Selling price',
            }),

            'minimum_stock': forms.NumberInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Minimum stock',
            }),

            'barcode': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Barcode',
            }),

        }


# =========================================================
# STOCK IN FORM
# =========================================================

class StockInForm(forms.Form):

    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        widget=forms.Select(attrs={
            'class': INPUT_CLASS,
        })
    )

    warehouse = forms.ModelChoiceField(
        queryset=Warehouse.objects.all(),
        widget=forms.Select(attrs={
            'class': INPUT_CLASS,
        })
    )

    quantity = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': INPUT_CLASS,
            'placeholder': 'Stock in quantity',
        })
    )

    reference_type = forms.CharField(
        required=False,
        initial='PURCHASE',
        widget=forms.TextInput(attrs={
            'class': INPUT_CLASS,
            'placeholder': 'Reference type',
        })
    )

    reference_id = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': INPUT_CLASS,
            'placeholder': 'Reference ID',
        })
    )


# =========================================================
# STOCK OUT FORM
# =========================================================

class StockOutForm(forms.Form):

    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        widget=forms.Select(attrs={
            'class': INPUT_CLASS,
        })
    )

    warehouse = forms.ModelChoiceField(
        queryset=Warehouse.objects.all(),
        widget=forms.Select(attrs={
            'class': INPUT_CLASS,
        })
    )

    quantity = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': INPUT_CLASS,
            'placeholder': 'Stock out quantity',
        })
    )

    reference_type = forms.CharField(
        required=False,
        initial='SALE',
        widget=forms.TextInput(attrs={
            'class': INPUT_CLASS,
            'placeholder': 'Reference type',
        })
    )

    reference_id = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': INPUT_CLASS,
            'placeholder': 'Reference ID',
        })
    )

    def clean(self):

        cleaned_data = super().clean()

        product = cleaned_data.get('product')
        warehouse = cleaned_data.get('warehouse')
        quantity = cleaned_data.get('quantity')

        if product and warehouse and quantity:

            stock = Stock.objects.filter(
                product=product,
                warehouse=warehouse
            ).first()

            if not stock:
                raise ValidationError(
                    'This product does not exist in this warehouse.'
                )

            if stock.quantity < quantity:
                raise ValidationError(
                    f'Only {stock.quantity} items available.'
                )

        return cleaned_data


# =========================================================
# STOCK TRANSFER FORM
# =========================================================

class StockTransferForm(forms.Form):

    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        widget=forms.Select(attrs={
            'class': INPUT_CLASS,
        })
    )

    from_warehouse = forms.ModelChoiceField(
        queryset=Warehouse.objects.all(),
        widget=forms.Select(attrs={
            'class': INPUT_CLASS,
        })
    )

    to_warehouse = forms.ModelChoiceField(
        queryset=Warehouse.objects.all(),
        widget=forms.Select(attrs={
            'class': INPUT_CLASS,
        })
    )

    quantity = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={
            'class': INPUT_CLASS,
            'placeholder': 'Transfer quantity',
        })
    )

    reference_type = forms.CharField(
        required=False,
        initial='TRANSFER',
        widget=forms.TextInput(attrs={
            'class': INPUT_CLASS,
        })
    )

    reference_id = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': INPUT_CLASS,
            'placeholder': 'Reference ID',
        })
    )

    def clean(self):

        cleaned_data = super().clean()

        product = cleaned_data.get('product')
        from_warehouse = cleaned_data.get('from_warehouse')
        to_warehouse = cleaned_data.get('to_warehouse')
        quantity = cleaned_data.get('quantity')

        if from_warehouse == to_warehouse:
            raise ValidationError(
                'Source and destination warehouse cannot be the same.'
            )

        if product and from_warehouse and quantity:

            stock = Stock.objects.filter(
                product=product,
                warehouse=from_warehouse
            ).first()

            if not stock:
                raise ValidationError(
                    'Product not available in source warehouse.'
                )

            if stock.quantity < quantity:
                raise ValidationError(
                    f'Only {stock.quantity} items available.'
                )

        return cleaned_data


# =========================================================
# STOCK ADJUSTMENT FORM
# =========================================================

class StockAdjustmentForm(forms.Form):

    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        widget=forms.Select(attrs={
            'class': INPUT_CLASS,
        })
    )

    warehouse = forms.ModelChoiceField(
        queryset=Warehouse.objects.all(),
        widget=forms.Select(attrs={
            'class': INPUT_CLASS,
        })
    )

    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': INPUT_CLASS,
            'placeholder': 'Adjusted quantity',
        })
    )

    reason = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': TEXTAREA_CLASS,
            'rows': 3,
            'placeholder': 'Adjustment reason',
        })
    )

    reference_type = forms.CharField(
        required=False,
        initial='ADJUSTMENT',
        widget=forms.TextInput(attrs={
            'class': INPUT_CLASS,
        })
    )

    reference_id = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': INPUT_CLASS,
            'placeholder': 'Reference ID',
        })
    )


# =========================================================
# STOCK SEARCH FILTER FORM
# =========================================================

class StockFilterForm(forms.Form):

    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': INPUT_CLASS,
        })
    )

    warehouse = forms.ModelChoiceField(
        queryset=Warehouse.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': INPUT_CLASS,
        })
    )


# =========================================================
# STOCK MOVEMENT FILTER FORM
# =========================================================

class StockMovementFilterForm(forms.Form):

    movement_type = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'All Movements'),
            ('IN', 'IN'),
            ('OUT', 'OUT'),
            ('TRANSFER', 'TRANSFER'),
            ('ADJUSTMENT', 'ADJUSTMENT'),
        ],
        widget=forms.Select(attrs={
            'class': INPUT_CLASS,
        })
    )

    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': INPUT_CLASS,
        })
    )

    warehouse = forms.ModelChoiceField(
        queryset=Warehouse.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': INPUT_CLASS,
        })
    )