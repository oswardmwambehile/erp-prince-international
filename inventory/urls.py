from django.urls import path

from . import views



urlpatterns = [

    path(
        "products/",
        views.product_list,
        name="product_list"
    ),
    path(
        "inventory_products/",
        views.inventory_product_list,
        name="inventory_product_list"
    ),
    path(
        "sales_products/",
        views.sales_product_list,
        name="sales_product_list"
    ),

    path(
        "products/create/",
        views.product_create,
        name="product_create"
    ),
    path(
        "inventory_products/create/",
        views.inventory_product_create,
        name="inventory_product_create"
    ),
path('inventory_dashboard/', views.inventory_dashboard, name='inventory_dashboard'),
    path(
        "inventory_products/<int:pk>/",
        views.inventory_product_detail,
        name="product_detail"
    ),
    path(
        "sales_products/<int:pk>/",
        views.sales_product_detail,
        name="sales_product_detail"
    ),
    path("inventory_categories/", views.category_page, name="category_page"),
    path('units/', views.unit_page, name='unit_page'),
    path("categories/", views.admin_category_page, name="admin_category_page"),
    path('admin_units/', views.admin_unit_page, name='admin_unit_page'),

    

    path(
        "products/<int:pk>/update/",
        views.product_update,
        name="product_update"
    ),

    path(
        "products/<int:pk>/delete/",
        views.product_delete,
        name="product_delete"
    ),
    path(
        'warehouses/',
        views.warehouse_list,
        name='warehouse_list'
    ),
    path(
        'inventory_warehouses/',
        views.inventory_warehouse_list,
        name='inventory_warehouse_list'
    ),

    path('stock/', views.stock_list, name='stock_list'),
    path('inventory_stock_list/', views.inventory_stock_list, name='inventory_stock_list'),
    path('stock-in/', views.stock_in, name='stock_in'),
    path('inventory_stock-in/', views.inventory_stock_in, name='inventory_stock_in'),
    path('stock-out/', views.stock_out, name='stock_out'),
    path('inventory_stock-out/', views.inventory_stock_out, name='inventory_stock_out'),
    path('stock-transfer/', views.stock_transfer, name='stock_transfer'),
    path('inventory_stock-transfer/', views.inventory_stock_transfer, name='inventory_stock_transfer'),
    path('stock-adjustment/', views.stock_adjustment, name='stock_adjustment'),
    path('inventory_stock-adjustment/', views.inventory_stock_adjustment, name='inventory_stock_adjustment'),
    path('stock-movements/', views.stock_movements, name='stock_movements'),
    path('inventory_stock-movements/', views.inventory_stock_movements, name='inventory_stock_movements'),
    path('inventory/low-stock/', views.low_stock_list, name='low_stock_list'),
]