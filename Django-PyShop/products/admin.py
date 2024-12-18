from django.contrib import admin
from .models import Product #import current models module for Product class
from .models import Offer

# Register your models here.

class ProductAdmin(admin.ModelAdmin): #create admin class for product
    list_display = ('name', 'price', 'stock') #what to display on the admin table
    #not displaying the image url

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

    #register Product class to admin panel
    #use ProductAdmin param so django knows how to display info
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
