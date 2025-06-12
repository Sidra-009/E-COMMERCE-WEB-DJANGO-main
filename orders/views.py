# Sidra You can do it dont giveup


from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Order
#from .forms import CheckoutForm  # You'll need to create this form
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import Order
from django.shortcuts import render

def orders_view(request):
    # Your view logic here
    return render(request, 'orders/orders.html')  # Make sure this template exists

@staff_member_required
def admin_order_list(request):
    """
    View for admin to see all orders
    """
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'orders/admin/list.html', {'orders': orders})
@csrf_exempt  # This decorator is often needed for webhooks
def payment_webhook(request):
    """
    Handle payment gateway webhook notifications
    """
    if request.method == 'POST':
        # Process the webhook data here
        # This will depend on your payment provider (Stripe, PayPal, etc.)
        
        # Example for a basic implementation:
        print("Webhook received:", request.POST)
        return HttpResponse(status=200)
    return HttpResponse(status=400)

def checkout_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/checkout_success.html', {
        'order': order,
        'title': f'Order #{order.id} Confirmation'
    })

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user  # If you have user authentication
            order.save()
            messages.success(request, "Order placed successfully!")
            return redirect('orders:order_detail', order_id=order.id)
    else:
        form = CheckoutForm()
    
    return render(request, 'orders/checkout.html', {'form': form})

# Create your views here.

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return render(request, 'orders/order_created.html', {'order': order})
    else:
        form = OrderForm()
    return render(request, 'orders/order_create.html', {'form': form})
def order_history(request):
    # Get all orders (or filter as needed)
    orders = Order.objects.filter(user=request.user).order_by('-created_at')  # Example query
    return render(request, 'orders/history.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/detail.html', {'order': order})

def order_create(request):
    # Your view logic here
    pass
def order_detail(request, order_id):
    return HttpResponse(f"Order ID: {order_id}")
