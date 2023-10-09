from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from products.models import Product


# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=100, unique=False)
    lname = models.CharField(max_length=100, unique=False)
    
    def __str__(self):
        return self.fname
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_products = models.PositiveIntegerField(default=0)
    

    
    def __str__(self):
        return f"{self.user.fname}'s cart"