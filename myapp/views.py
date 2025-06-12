from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import Http404

from .forms import CartAddProductForm, CustomUserCreationForm, CustomLoginForm
from cart.cart import Cart
from shop.models import Product
from .models import User
from django.shortcuts import render
from .models import Product  # make sure Product model is imported
from django.shortcuts import render, redirect
from django.db.models import Q
from myapp.models import Product  # Import your Product model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def search_view(request):
    query = request.GET.get('q', '').strip()
    
    if not query:
        # Redirect to home if search is empty
        return redirect('home')
    
    # Perform the search
    results = Product.objects.filter(
        Q(name__icontains=query) | 
        Q(description__icontains=query) |
        Q(category__name__icontains=query)
    ).distinct()
    
    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(results, 12)  # Show 12 products per page
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    context = {
        'query': query,
        'products': products,
        'result_count': results.count()
    }
    
    return render(request, 'search_results.html', context)

def product_list(request):
    products = Product.objects.all()  # sab products fetch karo
    return render(request, 'products.html', {'products': products})
# Authentication Views
class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'
    
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
        return super().form_valid(form)
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        return next_url or self.request.POST.get('next') or reverse_lazy('home')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# Main Pages
def home(request):
    context = {
        'featured_categories': [
            {'name': 'Electronics', 'url': 'myapp:phones'},
            {'name': 'Sports', 'url': 'myapp:sports'},
        ]
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# Product Categories
def electronics(request):
    return render(request, 'electronics.html')

def fashion(request):
    return render(request, 'fashion.html')

def home_living(request):
    return render(request, 'home_living.html')

def beauty(request):
    return render(request, 'beauty.html')

def sports_view(request):
    context = {'title': 'Sports Equipment', 'products': []}
    return render(request, 'sports/sports.html', context)

# Sub-categories
def phones_view(request):
    return render(request, 'phones.html')

def smart_phones(request):
    return render(request, 'smart_phones.html')

def laptops(request):
    return render(request, 'laptops.html')

def camera(request):
    return render(request, 'electronics/camera.html')

def mens_clothing(request):
    return render(request, 'mens_clothing.html')

def womens_clothing(request):
    return render(request, 'womens_clothing.html')

def skincare(request):
    return render(request, 'skincare.html')

def makeup(request):
    return render(request, 'makeup.html')

def haircare(request):
    return render(request, 'haircare.html')

# User Account
@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def order_list(request):
    return render(request, 'order_list.html')

@login_required
def wishlist(request):
    return render(request, 'wishlist.html')

# Cart Functionality
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

def checkout(request):
    return render(request, 'checkout.html')

# Error Handlers
def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)

def custom_500(request):
    return render(request, '500.html', {}, status=500)
# ... (keep all the existing imports and views above) ...

# Legal/Utility views
def privacy(request):
    return render(request, 'legal/privacy.html')

def terms(request):
    return render(request, 'legal/terms.html')

def cookies(request):
    return render(request, 'cookies.html')

def accessibility(request):
    return render(request, 'accessibility.html')

def security(request):
    return render(request, 'security.html')

# Shop related
def shop(request):
    return render(request, 'shop/shop.html')

def new_arrivals(request):
    return render(request, 'shop/new_arrivals.html')

def sale(request):
    return render(request, 'sale.html')

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
# ... (keep all existing imports and views) ...

# Fashion sub-categories
def shoes(request):
    return render(request, 'shoes.html')

# Home & Living sub-categories
def kitchen_view(request):
    return render(request, 'home-living/kitchen.html')

def decor_view(request):
    return render(request, 'decor.html')

def bedding_view(request):
    return render(request, 'home-living/bedding.html')

def furniture_view(request):
    return render(request, 'furniture.html')

# Electronics sub-categories
def audio(request):
    return render(request, 'audio.html')

def smart_home(request):
    return render(request, 'smart_home.html')

# Sports sub-categories
def gym_view(request):
    context = {'title': 'Gym Equipment', 'products': []}
    return render(request, 'sports/gym.html', context)

def yoga_view(request):
    context = {'title': 'Yoga Products', 'products': []}
    return render(request, 'sports/yoga.html', context)

def running_view(request):
    context = {'title': 'Running Gear', 'products': []}
    return render(request, 'sports/running.html', context)

# Beauty sub-categories
def vitamins(request):
    return render(request, 'beauty/vitamins.html')



# Home & Living category
def furniture(request):
    return render(request, 'furniture.html')

def kitchen(request):
    return render(request, 'home-living/kitchen.html')

def decor(request):
    return render(request, 'decor.html')

def bedding(request):
    return render(request, 'home-living/bedding.html')

# Electronics category
def laptops(request):
    return render(request, 'laptops.html')

def phones(request):
    return render(request, 'phones.html')

def smart_phones(request):
    return render(request, 'smart_phones.html')

def camera(request):
    return render(request, 'electronics/camera.html')

def audio(request):
    return render(request, 'audio.html')

def smart_home(request):
    return render(request, 'smart_home.html')

# Sports category
def sports(request):
    return render(request, 'sports/sports.html')

def gym(request):
    return render(request, 'sports/gym.html')

def yoga(request):
    return render(request, 'sports/yoga.html')

def running(request):
    return render(request, 'sports/running.html')

# Beauty category
def vitamins(request):
    return render(request, 'beauty/vitamins.html')
def index(request):
    return render(request, 'index.html')
def cart(request):
    return render(request, 'cart.html')
def team(request):
    return render(request, 'team.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def profile_view(request):
    return render(request, 'profile.html')
def  smart_phones_view(request):
    return render(request, 'smart_phones_view.html')

def  laptops_view(request):
    return render(request, 'laptops_view.html')
def  camera_view(request):
    return render(request, 'camera_view.html')
def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)
# In views.py
from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('home')  # Redirect to your home page
# In your views.py
def search_view(request):
    query = request.GET.get('q', '')
    # Your search logic here
    return render(request, 'search_results.html', {'results': results})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from .models import *
import random
import string

def generate_order_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

@login_required
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        cart.quantity += 1
        cart.save()
    
    return JsonResponse({'success': True, 'cart_count': request.user.cart_set.count()})

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    
    if created:
        return JsonResponse({'success': True, 'message': 'Added to wishlist'})
    return JsonResponse({'success': False, 'message': 'Already in wishlist'})

@login_required
def checkout(request):
    if request.method == 'POST':
        cart_items = Cart.objects.filter(user=request.user)
        
        if not cart_items.exists():
            return redirect('cart_view')
        
        total = sum(item.product.price * item.quantity for item in cart_items)
        order = Order.objects.create(
            user=request.user,
            order_number=generate_order_number(),
            total_amount=total,
            shipping_address=request.POST.get('shipping_address'),
            payment_method=request.POST.get('payment_method')
        )
        
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        
        cart_items.delete()
        return redirect('order_success', order_id=order.id)
    
    return render(request, 'shop/checkout.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()  # fetch all products
    return render(request, 'myapp/product_list.html', {'products': products})
def product_list(request):
    context = {
        # In myapp/views.py
        'trending_products': Product.objects.filter(badge='trending')[:8],
        'new_arrivals': Product.objects.order_by('-created')[:8],
        'bestsellers': Product.objects.filter(badge='sale')[:8],
        'featured_products': Product.objects.filter(featured=True)[:8],
    }
    return render(request, 'product_list.html', context)
from django.http import JsonResponse

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    data = {
        'id': product.id,
        'name': product.name,
        'price': float(product.price),
        'original_price': float(product.original_price) if product.original_price else None,
        'image': product.image.url,
        'images': [{'image': img.image.url} for img in product.images.all()],
        'rating': float(product.rating),
        'reviews': product.reviews,
        'description': product.description,
        'features': list(product.features.values_list('text', flat=True)),
        'badge': product.badge,
    }
    return JsonResponse(data)
