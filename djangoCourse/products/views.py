from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.

products_list = [
    {'id': 1, 'name': 'Laptop', 'price': 999.99, 'description': 'High-performance laptop'},
    {'id': 2, 'name': 'Mouse', 'price': 25.99, 'description': 'Wireless mouse'},
    {'id': 3, 'name': 'Keyboard', 'price': 49.99, 'description': 'Mechanical keyboard'},
]

def products(request):
    return render(request, 'products/index.html', {'products': products_list})

def product_detail(request, product_id):
    product = next((p for p in products_list if p['id'] == product_id), None)
    if product is None:        
        raise Http404("Product not found")
    return render(request, 'products/detail.html', {'product': product})