from rest_framework import serializers
from core.serializers import AddressSerializer
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
