from django.db import models
from django.contrib.auth.models import User



class Collection(models.Model):
    title = models.CharField(max_length=255) 
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']
     
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255 , null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2 , null=True)
    quantity = models.PositiveIntegerField(null=True)
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT) 
    def __str__(self) -> str:
        return self.title


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    birth_day = models.DateTimeField(null=True) 
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.ForeignKey)
    quantity = models.PositiveSmallIntegerField()   
    price = models.DecimalField(max_digits=6, decimal_places=3)
    placed_at = models.DateTimeField(auto_now_add=True)  
    staff = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    def __str__(self) -> str:
        return f'{self.product}'
     



