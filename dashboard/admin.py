from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','customer','order_quantity','payment_status','placed_at']
    
