# Sidra You can do it dont giveup

# Final corrected version
from django.urls import path
from . import views  # Consistent direct imports
from django.urls import path
from . import views

app_name = 'orders'  # this is important for namespace
app_name = 'orders'

urlpatterns = [

    

    path('', views.orders_view, name='orders'),
    # Order endpoints (ensure these views exist)
    path('create/', views.order_create, name='order_create'),
    path('history/', views.order_history, name='order_history'),
    path('detail/<int:order_id>/', views.order_detail, name='order_detail'),
    
    # Checkout endpoints
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/success/<int:order_id>/', views.checkout_success, name='checkout_success'),
    
    # Payment webhook (uncomment when ready)
    # path('payment/webhook/', views.payment_webhook, name='payment_webhook'),
]