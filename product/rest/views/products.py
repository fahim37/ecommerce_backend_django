from rest_framework import generics

from product.models import Product
from product.rest.serializers.products import ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    print("test git workflows")
