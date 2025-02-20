from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order, OrderItem, Category
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib import messages


def home(request):
    categories = Category.objects.all()  # Fetch all categories
    best_sellers = Product.objects.all()[:4]  # Get top 3 products
    return render(request, 'store/home.html', {'categories': categories, 'best_sellers': best_sellers})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.all()

    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=selected_category)

    return render(request, 'store/product_list.html', {
        'products': products, 'categories': categories, 'selected_category': selected_category})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1
    request.session['cart'] = cart
    messages.success(request, f'Added {product.name} to cart.')
    return redirect('product_list')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
        messages.success(request, 'Removed product from cart.')
    return redirect('cart')


def cart(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        product.quantity = quantity
        product.total_price = product.price * quantity
        total += product.total_price
        products.append(product)
    return render(request, 'store/cart.html', {'products': products, 'total': total})


@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.info(request, 'Your cart is empty.')
        return redirect('product_list')

    if request.method == 'POST':
        # Simulate payment process.
        # In production, integrate with a real payment gateway.

        # Create an Order
        order = Order.objects.create(user=request.user, is_paid=True)
        for product_id, quantity in cart.items():
            product = get_object_or_404(Product, id=product_id)
            OrderItem.objects.create(order=order, product=product, quantity=quantity)

        # Clear the cart after order placement
        request.session['cart'] = {}

        messages.success(request, 'Order placed successfully!')
        return redirect('order_confirmation', order_id=order.id)

    # If GET, show checkout summary
    products = []
    total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        product.quantity = quantity
        product.total_price = product.price * quantity
        total += product.total_price
        products.append(product)

    return render(request, 'store/checkout.html', {'products': products, 'total': total})


@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'store/order_confirmation.html', {'order': order})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
