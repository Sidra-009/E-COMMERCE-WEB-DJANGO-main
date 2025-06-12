
from django.urls import path
from . import views

app_name = 'shop'  # This namespace is crucial

urlpatterns = [
    path('', views.home, name='home'),
    path('fashion/', views.fashion_view, name='fashion'),
    path('mens-clothing/', views.mens_clothing_view, name='mens_clothing'),
    path('womens-clothing/', views.womens_clothing_view, name='womens_clothing'),
    path('shoes/', views.shoes_view, name='shoes'),
    path('accessories/', views.accessories_view, name='accessories'),
    path('jewelry/', views.jewelry_view, name='jewelry'),
    path('bags-wallets/', views.bags_wallets_view, name='bags_wallets'),
     path('contact/', views.contact, name='contact'),
    path('shipping/', views.shipping, name='shipping'),
    path('returns/', views.returns, name='returns'),
    path('size-guide/', views.size_guide, name='size_guide'),
    path('track-order/', views.track_order, name='track_order'),
    path('faq/', views.faq, name='faq'),
      # Company URLs
    path('about/', views.about, name='about'),
    path('careers/', views.careers, name='careers'),
    path('press/', views.press, name='press'),
    path('affiliate/', views.affiliate, name='affiliate'),
    path('sustainability/', views.sustainability, name='sustainability'),
    path('investors/', views.investors, name='investors'),
]