from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class AddCash(models.Model):
    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    source=models.CharField(max_length=100)
    datetime=models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField(max_length=200)
    
    
class Expenses(models.Model):
    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    
    description=models.TextField(max_length=200)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    datetime=models.DateTimeField(default=timezone.now)