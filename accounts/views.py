from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


# Homepage
def index(request):
    return render(request, 'index.html')

# About Page
def about(request):
    return render(request, 'about.html')

# Services Page
def services(request):
    return render(request, 'services.html')

# Products Page
def products(request):
    return render(request, 'products.html')

# Contact Page
def contact_us(request):
    return render(request, 'contact.html')

# Team Members Page
def team_members(request):
    return render(request, 'team.html')

# All Dishes
def all_dishes(request):
    return render(request, 'dishes.html')

# Single Dish View (dynamic based on dish ID)
def single_dish(request, id):
    # You can later fetch the dish from the database using this id
    return render(request, 'single_dish.html', {'dish_id': id})

# Dashboard (after login)
def dashboard(request):
    return render(request, 'dashboard.html')

# Search Functionality
def search(request):
    query = request.GET.get('q')
    return render(request, 'search_results.html', {'query': query})

# Payment Success Page
def payment_done(request):
    return render(request, 'payment_done.html')

# Payment Cancel Page
def payment_cancel(request):
    return render(request, 'payment_cancel.html')

# Custom Sign In
def signin(request):
    return render(request, 'login.html')

# Custom Logout
def user_logout(request):
    # You can use Django's logout logic here
    return redirect('index')

# User Registration
def register(request):
    return render(request, 'register.html')

# Check if User Exists (AJAX call)
def check_user_exists(request):
    return HttpResponse("Check logic goes here")
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to home after login
        else:
            from django.contrib import messages
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')
def home(request):
    return render(request, 'home.html')


def home(request):
    return render(request, 'home.html') 
