from django.http import HttpResponse  # With this we can create a HTTP Response to return to the client/browser
from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    # We use this to get our products from our database
    products = Product.objects.all()
    # Displaying it on the products page
    # We want to display our index.html file
    # We want to display the products so we pass them as a dictionary
    return render(request, 'index.html',
                  {'products': products})


# Request for the /new page
def new(request):
    return HttpResponse('New Products')

