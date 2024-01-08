from django.urls import path
from product.rest.views.products import ProductListCreateView

urlpatterns = [
    path("", ProductListCreateView.as_view(), name="product-list-create"),
]
