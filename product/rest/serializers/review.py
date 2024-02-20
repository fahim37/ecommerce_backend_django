from core.models import Review
from rest_framework import serializers

from product.models import Product


class ReviewSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Review
        fields = "__all__"
