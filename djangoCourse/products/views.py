from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
# Create your views here.


# products_list = [
#     {'id': 1, 'name': 'Laptop', 'price': 999.99, 'description': 'High-performance laptop', 'image': 'laptop.png'},
#     {'id': 2, 'name': 'Mouse', 'price': 25.99, 'description': 'Wireless mouse', 'image': 'mouse.png'},
#     {'id': 3, 'name': 'Keyboard', 'price': 49.99, 'description': 'Mechanical keyboard', 'image': 'keyboard.png'},
# ]



def product_detail(request, product_id):
    products = Product.objects.all()  #filter 
    product = [p for p in products if p.id == product_id]
    if not product:        
        raise Http404("Product not found")
    return render(request, 'products/detail.html', {'product': product[0]})


def products_list(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})


def manage_products(request):
    products = Product.objects.all()
    return render(request, 'products/manage.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        
        Product.objects.create(
            name=name,
            price=price,
            description=description,
            image=image
        )
        return redirect('products:manage_products')
    
    return render(request, 'products/add_product.html')


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('products:manage_products')