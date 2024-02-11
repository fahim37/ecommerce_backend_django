from rest_framework import serializers
from product.models import Category
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "price", "image", "category", "stock")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "name"
