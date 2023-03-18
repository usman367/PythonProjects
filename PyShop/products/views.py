from django.http import HttpResponse # With this we can create a HTTP Response to return to the client/browser
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('Hello World')


# Request for the /new page
def new(request):
    return HttpResponse('New Products')

