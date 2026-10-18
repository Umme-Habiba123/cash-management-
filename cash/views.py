from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from  .forms import *


# Create your views here.

@login_required
def home(request):
    income = AddCash.objects.filter(user=request.user)
    expenses = Expenses.objects.filter(user=request.user)

    return render(request,'home.html',{
        'income': income,
        'expenses':expenses,
    })
    
    
@login_required
def profile(request):
    return render(request, 'profile.html')


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


def dashboard(request):
    income=AddCash.objects.filter(user=request.user)
    expenses=Expenses.objects.filter(user=request.user)
    
    total_income=sum(item.amount for item in income)
    total_expense=sum(item.amount for item in expenses)
    
    balance=total_income-total_expense
    
    return render(request, 'dashboard.html',{
        'income': income,
        'expenses': expenses,
        'total_income':total_income,
        'total_expense': total_expense,
        'balance': balance,
    })



def add_cash(request):
    form=AddCashForm(request.POST or None)
    
    if form.is_valid():
        cash=form.save(commit=False)
        cash.user=request.user
        cash.save()
        return redirect('dashboard')
    
    return render(request, 'transactionForm.html',{
        'form':form
    })
    
    
def add_expense(request):
    form=ExpenseForm(request.POST or None)
    
    if form.is_valid():
        expense=form.save(commit=False)
        expense.user=request.user
        expense.save()
        
        return redirect('dashboard')
    
    return render(request, 'transactionForm.html',{
        'form': form,
        'title': 'Add Expense'
    })