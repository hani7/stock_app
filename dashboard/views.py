from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')


def staff(request):
    return render(request, 'dashboard/staff.html')


def product(request):
    items = Product.objects.all() 
    #items = Product.objects.raw('SELECT * FROM product')

    context = {
        'items' : items,
    }
    return render(request, 'dashboard/product.html' , context)


def order(request):
    return render(request, 'dashboard/order.html')

def profile(request):
    return render(request, 'dashboard/profile.html')