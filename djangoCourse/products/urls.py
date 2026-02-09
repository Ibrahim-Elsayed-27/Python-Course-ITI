from django.urls import path
from products.views import product_detail, products_list, manage_products, add_product, delete_product

app_name = 'products'
urlpatterns = [
    path('', products_list, name='product_list'),
    path('<int:product_id>/', product_detail, name='product_detail'),
    path('manage/', manage_products, name='manage_products'),
    path('add/', add_product, name='add_product'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
]