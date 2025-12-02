from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import ProductForm

@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manager')
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})


@login_required
def manager_dashboard(request):
    products = Product.objects.all()
    return render(request, 'store/manager.html', {'products': products})

# ---------- PUBLIC VIEWS ----------

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def product_list(request):
    category = request.GET.get('category')
    products = Product.objects.all()
    if category:
        products = products.filter(category=category)
    context = {
        'products': products,
        'selected_category': category,
    }
    return render(request, 'store/product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

# ---------- SELLER (MOBILE) VIEWS ----------

def _seller_is_logged_in(request):
    """Small helper: checks if seller already logged in with PIN."""
    return request.session.get('seller_logged_in', False)

def seller_login(request):
    """PIN login page for IKKAT STORE MANAGER."""
    error = None

    if request.method == 'POST':
        pin = request.POST.get('pin')
        if pin == settings.SELLER_PIN:
            request.session['seller_logged_in'] = True
            return redirect('seller_dashboard')
        else:
            error = "Incorrect PIN. Try again."

    return render(request, 'store/seller_login.html', {'error': error})

def seller_logout(request):
    """Logout seller session."""
    request.session.pop('seller_logged_in', None)
    return redirect('seller_login')

def seller_dashboard(request):
    """List of products to edit – only for logged in seller."""
    if not _seller_is_logged_in(request):
        return redirect('seller_login')

    products = Product.objects.all().order_by('-id')
    return render(request, 'store/seller_dashboard.html', {'products': products})

def seller_edit_product(request, pk):
    """Edit existing product – change name, price, image."""
    if not _seller_is_logged_in(request):
        return redirect('seller_login')

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        if name:
            product.name = name
        if price:
            try:
                # If price is decimal field in your model, this will cast properly
                product.price = price
            except Exception:
                pass  # ignore bad input

        if image:
            product.image = image

        product.save()
        return redirect('seller_dashboard')

    return render(request, 'store/seller_edit_product.html', {'product': product})
def seller_add_product(request):
    if not _seller_is_logged_in(request):
        return redirect('seller_login')

    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        image = request.FILES.get("image")

        if name and price and image:
            Product.objects.create(name=name, price=price, image=image)
            return redirect('seller_dashboard')

    return render(request, 'store/seller_add_product.html')

