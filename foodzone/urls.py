# Sidra You can do it dont giveup
from django.contrib.auth import views as auth_views
from myapp import views
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import privacy, register, terms
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.contrib.auth import views as auth_views
from myapp.views import CustomLogoutView
from django.contrib.auth.views import LogoutView 
from django.conf import settings
from django.conf.urls.static import static # Add this import
urlpatterns = [
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
     #   path('admin/', admin.site.urls),
    
    # Home
    path('', views.home, name='home'),
     path('search/', views.search_view, name='search'),
    
    # Fashion Category
    path('fashion/', views.fashion, name='fashion'),
    path('mens-clothing/', views.mens_clothing, name='mens_clothing'),
    path('womens-clothing/', views.womens_clothing, name='womens_clothing'),
    path('shoes/', views.shoes, name='shoes'),
    
    # Electronics Category
    path('electronics/', views.electronics, name='electronics'),
    path('laptops/', views.laptops, name='laptops'),
    path('camera/', views.camera, name='camera'),
    path('smart-phones/', views.smart_phones, name='smart_phones'),
    
    # Home & Living Category
    path('home-living/', views.home_living, name='home_living'),
    path('furniture/', views.furniture, name='furniture'),
    path('kitchen/', views.kitchen, name='kitchen'),
    path('bedding/', views.bedding, name='bedding'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    
    # Beauty & Health Category
    path('beauty/', views.beauty, name='beauty'),
    path('skincare/', views.skincare, name='skincare'),
    path('makeup/', views.makeup, name='makeup'),
    path('haircare/', views.haircare, name='haircare'),
    
    # User Account
    path('profile/', views.profile, name='profile'),
    path('orders/', views.order_list, name='order_list'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('index/', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    
    
     path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),

        # Additional Pages
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('orders/', include('orders.urls')),
    path('fashion/', views.fashion, name='fashion'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('terms/', terms, name='terms'),
    path('privacy/', privacy, name='privacy'),
    path('accounts/', include('django.contrib.auth.urls')),
    

    
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.home, name='home'),
        path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('cart/', include('cart.urls', namespace='cart')),
     path('smart-phones/', views.smart_phones_view, name='smart_phones'),


    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('shop/', include('shop.urls')),
   # path('accounts/', include('accounts.urls')),

    path('decor/', views.decor_view, name='decor'),  # Add this line
    path('kitchen/', views.kitchen_view, name='kitchen'),
    path('bedding/', views.bedding_view, name='bedding'),
    # ... existing URLs ...

    path('fashion/login/', auth_views.LoginView.as_view(template_name='fashion/login.html'), name='fashion_login'),
    path('electronics/login/', auth_views.LoginView.as_view(template_name='electronics/login.html'), name='electronics_login'),
    path('skincare/login/', auth_views.LoginView.as_view(template_name='skincare/login.html'), name='skincare_login'),
    path('haircare/login/', auth_views.LoginView.as_view(template_name='haircare/login.html'), name='haircare_login'),
    # Add more as needed...


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Your existing URL patterns here...

if not settings.DEBUG:  # Only enable in production
    handler404 = 'myapp.views.handler404'
    handler500 = 'myapp.views.handler500'
