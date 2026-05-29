from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.customer_list,
        name='customer_list'
    ),
    path(
        'customer/',
        views.sales_customer_list,
        name='sales_customer_list'
    ),

    path(
        'create/',
        views.customer_create,
        name='customer_create'
    ),
    path(
        'sales_create/',
        views.sales_customer_create,
        name='sales_customer_create'
    ),

    path(
        '<int:pk>/',
        views.customer_detail,
        name='customer_detail'
    ),
    path(
        'sales<int:pk>/',
        views.sales_customer_detail,
        name='sales_customer_detail'
    ),

    path(
        '/<int:pk>/update/',
        views.customer_update,
        name='customer_update'
    ),
    path(
        '/<int:pk>/update/',
        views.sales_customer_update,
        name='sales_customer_update'
    ),

    path(
        '/<int:pk>/delete/',
        views.customer_delete,
        name='customer_delete'
    ),

    path(
    '/suppliers/',
    views.supplier_list,
    name='supplier_list'
),

path(
    '/suppliers/create/',
    views.supplier_create,
    name='supplier_create'
),

path(
    '/suppliers/<int:pk>/',
    views.supplier_detail,
    name='supplier_detail'
),

path(
    '/suppliers/<int:pk>/update/',
    views.supplier_update,
    name='supplier_update'
),

path(
    '/suppliers/<int:pk>/delete/',
    views.supplier_delete,
    name='supplier_delete'
),

]