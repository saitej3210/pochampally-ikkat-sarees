from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    # Show latest 8 products on home page
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def product_list(request):
    # Show all products, with optional category filter
    category = request.GET.get('category')
    products = Product.objects.all().order_by('-created_at')
    if category:
        products = products.filter(category=category)

    context = {
        'products': products,
        'selected_category': category,
    }
    return render(request, 'store/product_list.html', context)

def product_detail(request, pk):
    # Show a single product
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})
