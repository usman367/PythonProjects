from django.contrib import admin
from .models import Product, Offer  # Get the products module and the Offer


# Wasn't working when we added a new product
# So I had to use django 2.1.5
# Delete the SQLite database
# Run the migrations
# The it worked
# https://stackoverflow.com/questions/53637182/django-no-such-table-main-auth-user-old?rq=1


# admin.ModelAdmin, which provides functionality for managing models in the admin area
# This will allow us to create a products table
class ProductAdmin(admin.ModelAdmin):
    # list_display allows you to add columns to the table
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
