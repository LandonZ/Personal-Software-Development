#create urls python file to map urls to functions
from django.urls import path #import path function
from . import views #from current folder import views.
# Has many views module so need to do "from ."

#must have urlpatterns list for django
#takes in various urls
urlpatterns = [
    #root of app (like /products/....)
    # But the root is THE HOME PAGE PRODUCTS, so nothing after products/
    # reference the index function from views.
    # not calling function, PASS REFERENCE TO IT

    #/products/ page
    path('', views.index),
    #the url pattern for new. root will be 'new', after products/
    #/products/new page
    path('new', views.new)
]