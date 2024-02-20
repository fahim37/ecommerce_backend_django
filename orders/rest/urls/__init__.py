# products.py
from django.urls import path, include

urlpatterns = [
    path("", include("orders.rest.urls.orders")),
]
