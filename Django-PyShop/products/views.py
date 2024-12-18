from django.http import HttpResponse #Http response class
from django.shortcuts import render #importing render function
from .models import Product

#for the main page of the app
# /products -> index
# Map the URL (Uniform Resource Locater, or Address) to index
def index(request): #take in http request passed by views function
    # DISPLAYING PRODUCTS FROM DATABASE TO WEBSITE
    products = Product.objects.all() #get all products in database

    #want to create templates for index function
    # rendering template from templates
    return render(request, 'index.html',
                  # dictionary of data passed to template
                  {'products': products})

#when requesting for the new page
def new(request):
    return HttpResponse('New Products')

