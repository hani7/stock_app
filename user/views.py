from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


def register(request):
    if request.method == 'POST': 
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else : 
        form = CreateUserForm() 
    context = {
        'form' : form,
    }
    return render(request, 'user/register.html' , context)