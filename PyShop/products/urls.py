# With this we can map a url to a function
from django.urls import path
# Import the views module into this module ( . means this folder)
from . import views



# /products will represent the root of the app
urlpatterns = [
    # Represents the roots of our app
    # We pass a reference to the index function from views we crated (we don't call it)
    # Django will call the function at runtime when the client sends a HTTP Request to the server
    path('', views.index),
    # Passing a reference for the /new page
    path('new', views.new)
]