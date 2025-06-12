from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.cart import Cart
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
def fashion_view(request):
    return render(request, 'shop/fashion.html')  # This is correct

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})

def home(request):
    return render(request, 'shop/home.html')

@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        # Process order form
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        return redirect('orders:order_detail', order.id)
    return render(request, 'orders/create.html', {'cart': cart})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/detail.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created')
    return render(request, 'orders/history.html', {'orders': orders})



def home(request):
    return render(request, 'shop/home.html')

def fashion_view(request):  # Changed from fashion_view to fashion
    return render(request, 'shop/fashion.html')

def mens_clothing_view(request):
    return render(request, 'shop/mens_clothing.html')

def womens_clothing_view(request):
    return render(request, 'shop/womens_clothing.html')

def shoes_view(request):
    return render(request, 'shop/shoes.html')

def accessories_view(request):
    return render(request, 'shop/accessories.html')

def  jewelry_view(request):
    return render(request, 'shop/jewelry.html')

def bags_wallets_view(request):
    return render(request, 'shop/bags_wallets.html')
# Add other view functions as needed
from django.shortcuts import render

def contact(request):
    return render(request, 'shop/contact.html')

def shipping(request):
    return render(request, 'shop/shipping.html')

def returns(request):
    return render(request, 'shop/returns.html')

def size_guide(request):
    return render(request, 'shop/size_guide.html')

def track_order(request):
    return render(request, 'shop/track_order.html')

def faq(request):
    return render(request, 'shop/faq.html')

# ... your existing view functions ...from django.shortcuts import render

def contact(request):
    return render(request, 'shop/contact.html')

def shipping(request):
    return render(request, 'shop/shipping.html')

def returns(request):
    return render(request, 'shop/returns.html')

def size_guide(request):
    return render(request, 'shop/size_guide.html')

def track_order(request):
    return render(request, 'shop/track_order.html')

def faq(request):
    return render(request, 'shop/faq.html')

# Customer Service Views
def contact(request):
    return render(request, 'shop/contact.html')

def shipping(request):
    return render(request, 'shop/shipping.html')

def returns(request):
    return render(request, 'shop/returns.html')

def size_guide(request):
    return render(request, 'shop/size_guide.html')

def track_order(request):
    return render(request, 'shop/track_order.html')

def faq(request):
    return render(request, 'shop/faq.html')

# Company Views
def about(request):
    return render(request, 'shop/about.html')

def careers(request):
    return render(request, 'shop/careers.html')

def press(request):
    return render(request, 'shop/press.html')

def affiliate(request):
    return render(request, 'shop/affiliate.html')

def sustainability(request):
    return render(request, 'shop/sustainability.html')

def investors(request):
    return render(request, 'shop/investors.html')

# ... your existing view functions ...