
from django.contrib import admin
from .product import Product
from .catogery import Catogery
from .customer import Customer
# Register your models here.
class Catogeryinfo(admin.ModelAdmin):
    list_display=['name']

class Productinfo(admin.ModelAdmin):
    list_display=['name','price']

class Customerinfo(admin.ModelAdmin):
    list_display=['firstname','lastname','email']
    
admin.site.register(Product,Productinfo),
admin.site.register(Catogery,Catogeryinfo),
admin.site.register(Customer,Customerinfo)
# Register your models here.
