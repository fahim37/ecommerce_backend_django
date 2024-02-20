from orders.models import Cart
from rest_framework import serializers
from product.models import Product


class CartSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Cart
        fields = ["product", "quantity"]
