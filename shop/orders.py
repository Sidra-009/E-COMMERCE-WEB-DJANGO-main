from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # Order creation
    path('create/', views.order_create, name='order_create'),
    
    # Order history
    path('history/', views.order_history, name='order_history'),
    
    # Order detail
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    
    # Order payment
    path('<int:order_id>/payment/', views.order_payment, name='order_payment'),
    
    # Order cancellation
    path('<int:order_id>/cancel/', views.order_cancel, name='order_cancel'),
    
    # Admin actions
    path('<int:order_id>/process/', views.order_process, name='order_process'),
    path('<int:order_id>/complete/', views.order_complete, name='order_complete'),
]