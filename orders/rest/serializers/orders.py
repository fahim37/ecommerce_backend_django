from rest_framework import serializers
from orders.models import Order, OrderProduct


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = OrderProduct
        fields = ("order_item_id", "product_id", "product_name", "quantity")


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
