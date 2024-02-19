from rest_framework import serializers

from product.models import Category
from product.models import Product

from versatileimagefield.serializers import VersatileImageFieldSerializer


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    image = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
            ("medium", "crop__400x400"),
        ],
        required=False,
    )

    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "image", "category", "stock"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]
