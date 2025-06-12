from django.db import models
from django.conf import settings
from myapp.models import Product
from django.contrib.auth.models import User

import uuid

def generate_order_number():
    return uuid.uuid4().hex[:16].upper()

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ]
    


    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='orders')



    order_number = models.CharField(
        max_length=32,
        unique=True,
        default=generate_order_number,
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    shipping_address = models.TextField()
    payment_method = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Order #{self.order_number} - {self.status}"

    class Meta:
        ordering = ['-created_at']

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='orders_orderitems')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order: {self.order.order_number})"