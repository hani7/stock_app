from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

# Create your views here.

@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required
def product(request):
    items = Product.objects.all() 
    #items = Product.objects.raw('SELECT * FROM product')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
    else : 
        form = ProductForm()    


    context = {
        'items' : items,
        'form':  form,
    }
    return render(request, 'dashboard/product.html' , context)

@login_required
def order(request):
    return render(request, 'dashboard/order.html')

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')