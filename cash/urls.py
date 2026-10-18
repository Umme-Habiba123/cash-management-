from django.urls import path 
from .views import *


urlpatterns = [
    path('', home , name='home'),
    path('register', register, name='register'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('add-cash', add_cash, name='add_cash'),
    path('add-expense', add_expense, name='add_expense'),
    path('dashboard', dashboard, name='dashboard'),
    path('profile', profile, name='profile'),
]
