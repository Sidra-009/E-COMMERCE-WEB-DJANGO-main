from django.conf import settings
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import search_view

app_name = 'myapp'

urlpatterns = [
    path('search/', search_view, name='search_view'),
     path('products/', views.product_list, name='product_list'),

    # Home and core pages
     path('smart-phones/', views.smart_phones_view, name='smart_phones'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
     path('audio/', views.audio, name='audio'),
        # ... your other URL patterns ...
    path('smart-home/', views.smart_home, name='smart_home'),
    
    # Fashion
    path('fashion/', views.fashion, name='fashion'),
    path('fashion/mens-clothing/', views.mens_clothing, name='mens_clothing'),
    path('fashion/womens-clothing/', views.womens_clothing, name='womens_clothing'),

    # Electronics
    path('electronics/', views.electronics, name='electronics'),
    path('electronics/phones/', views.phones_view, name='phones'),
    path('electronics/laptops/', views.laptops_view, name='laptops'),
    path('electronics/camera/', views.camera_view, name='camera'),
    path('electronics/smart-phones/', views.smart_phones_view, name='smart_phones'),
    # In myapp/urls.py
    path('electronics/smart-phones/', views.smart_phones_view, name='smart_phones'),

    path('beauty/', views.beauty, name='beauty'),
     path('beauty-health/', views.beauty),
    path('skincare/', views.skincare, name='skincare'),
    path('makeup/', views.makeup, name='makeup'),
    path('haircare/', views.haircare, name='haircare'),
    path('vitamins/', views.vitamins, name='vitamins'),

    # Sports & Fitness
    path('sports/', views.sports_view, name='sports'),
    path('sports/gym/', views.gym_view, name='gym'),
    path('sports/yoga/', views.yoga_view, name='yoga'),
    path('sports/running/', views.running_view, name='running'),

    # Home & Living
    path('home-living/', views.home_living, name='home_living'),
    path('home-living/furniture/', views.furniture_view, name='furniture'),
    path('home-living/decor/', views.decor_view, name='decor'),
    path('home-living/kitchen/', views.kitchen_view, name='kitchen'),
    path('home-living/bedding/', views.bedding_view, name='bedding'),

    # Shopping
    path('sale/', views.sale, name='sale'),
    path('shop/', views.shop, name='shop'),
    path('new-arrivals/', views.new_arrivals, name='new_arrivals'),

    # User accounts (updated paths)
    path('login/', views.login, name='login'), 
    path('register/', views.register, name='register'),
    

    # Checkout and legal
    path('checkout/', views.checkout, name='checkout'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('cookies/', views.cookies, name='cookies'),
   # path('gdpr/', views.gdpr, name='gdpr'),
    path('accessibility/', views.accessibility, name='accessibility'),
    path('security/', views.security, name='security'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)