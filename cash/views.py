from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from  .forms import *


# Create your views here.


def home(request):
   
    return render(request,'home.html',)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {
        'form': form
    })
    

def user_login(request):
    form = LoginForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user:
                login(request, user)
                return redirect('home')
            else:
                form=LoginForm()
    return render(request, 'login.html', {'form': form})





def user_logout(request):
    logout(request)
    return redirect('login')



