from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def staff(request):
    return render(request, 'staff.html')