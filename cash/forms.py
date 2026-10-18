from django import forms
from django.contrib.auth.forms import UserCreationForm, User, AuthenticationForm
from .models import *

    
class RegisterForm(UserCreationForm):
    
    username=forms.CharField(label='Username', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter Login'
        }
    ))
    
    email=forms.CharField(label='Email', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Write Your Email'
        }
    ))
    
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Password'
        }
    ))
    
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Confirm Password'
        }
    ))
    
   
    class Meta:
        model=User
        fields=['username', 'email','password1', 'password2']
    
    
class LoginForm(AuthenticationForm):    
     username=forms.CharField(label='Username', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter Login'
        }
    ))
     
     email=forms.CharField(label='Email', widget=forms.TextInput(
         attrs={
             'class':'form-control',
             'placeholder':'Enter email'
         }
     ))
     
     password=forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Password'
        }
    ))
    
    
class AddCashForm(forms.ModelForm):
    class Meta:
        model = AddCash
        fields = ['source', 'datetime', 'amount', 'description']
        widgets = {
            'datetime': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }     
        
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['description', 'amount', 'datetime']
        widgets = {
            'datetime': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }     
        
        