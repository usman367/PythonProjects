"""pyshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # Added the includes function

urlpatterns = [
    path('admin/', admin.site.urls),
    # Any urls that start with products/ ,delegate them to the products app
    # So any urls that start with products/ send them to the urls module in the products app
    # The server will only work now on http://127.0.0.1:8000/products/
    path('products/', include('products.urls'))
]
