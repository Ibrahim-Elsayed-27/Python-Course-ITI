from django.urls import path
from products.views import products, product_detail

app_name = 'products'
urlpatterns = [
    path('', products, name='product_list'),
    path('<int:product_id>/', product_detail, name='product_detail'),
]