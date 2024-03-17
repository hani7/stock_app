from django.contrib import admin
from .models import Product,Collection,Order
from .custom_tags import currency
from django.contrib.auth.models import User
from django.contrib.auth.models import Group



admin.site.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title']
    
    def products_count (self , collection):
        return collection.products_count
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title' ,'collection' , 'formatted_price', 'quantity' ,'last_update')
    list_filter = ['collection']
    
    def formatted_price(self, obj):
        return currency(obj.price)
    formatted_price.short_description = 'Price'
    
    class Meta :
        verbose_name_plural ='Products'
    
admin.site.register(Product , ProductAdmin) 

admin.site.register(Order) 
   

