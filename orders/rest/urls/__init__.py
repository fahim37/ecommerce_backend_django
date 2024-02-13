# products.py
from django.urls import path, include

urlpatterns = [
    path("", include("product.rest.urls.products")),
    path("category/", include("product.rest.urls.category")),
]
