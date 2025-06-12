from django.db import models
from django.contrib.auth.models import User

class MainCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = "Main Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = "Sub Categories"
        ordering = ['main_category', 'name']
    
    def __str__(self):
        return f"{self.main_category.name} - {self.name}"

class Product(models.Model):
    BADGE_CHOICES = [
        ('', 'None'),
        ('trending', 'Trending'),
        ('new', 'New'),
        ('sale', 'Sale'),
    ]
    
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    badge = models.CharField(max_length=20, choices=BADGE_CHOICES, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    sales_count = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.name
    
    def get_display_price(self):
        return f"${self.price:.2f}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    shipping_address = models.TextField(blank=True, null=True)
    billing_address = models.TextField(blank=True, null=True)
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return f'Order {self.id} - {self.user.username}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity}x {self.product.name}"
    
    def get_cost(self):
        return self.price * self.quantity

class UserActivity(models.Model):
    ACTIVITY_TYPES = [
        ('LOGIN', 'Login'),
        ('LOGOUT', 'Logout'),
        ('REGISTER', 'Register'),
        ('ADD_TO_CART', 'Add to Cart'),
        ('REMOVE_FROM_CART', 'Remove from Cart'),
        ('CHECKOUT', 'Checkout'),
        ('PAGE_VIEW', 'Page View'),
        ('PRODUCT_VIEW', 'Product View'),
        ('SEARCH', 'Search'),
    ]
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    activity_type = models.CharField(
        max_length=20,
        choices=ACTIVITY_TYPES,
        default='PAGE_VIEW'
    )
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    device = models.CharField(max_length=255, blank=True, null=True)
    browser = models.CharField(max_length=100, blank=True, null=True)
    os = models.CharField(max_length=100, blank=True, null=True)
    additional_data = models.JSONField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # For product-related activities
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    # For order-related activities
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    class Meta:
        verbose_name_plural = "User Activities"
        ordering = ['-timestamp']
    
    def __str__(self):
        user = self.user.username if self.user else 'Anonymous'
        return f"{user} - {self.get_activity_type_display()} at {self.timestamp}"