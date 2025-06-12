from .cart import Cart
# cart/context_processors.py
from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}
