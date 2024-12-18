from django.db import models

# Create your models here.

#new class Product
#inherit the Model class from django. So can read/store from database, etc
class Product(models.Model):
    # set variables to CharField (field that can contain textual data
    #give max_length so malicious user won't store product with huge name
    name = models.CharField(max_length=255)
    #field that can contain floating numbers
    price = models.FloatField()
    stock = models.IntegerField()
    #standard max length for urls
    image_url = models.CharField(max_length=2083)

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
