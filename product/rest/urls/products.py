from django.urls import path
from product.rest.views.products import ProductList

urlpatterns = [
    path("", ProductList.as_view(), name="product-list-create"),
]
