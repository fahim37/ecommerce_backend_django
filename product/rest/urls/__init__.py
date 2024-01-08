# products.py
from django.urls import path, include

urlpatterns = [
    path("", include("product.rest.urls.products")),
]
