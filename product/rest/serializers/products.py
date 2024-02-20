from rest_framework import serializers

from product.models import Category
from product.models import Product

from versatileimagefield.serializers import VersatileImageFieldSerializer

from product.rest.serializers.review import ReviewSerializer


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
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="slug", required=False
    )
    reviews = ReviewSerializer(source="review_set", many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]
