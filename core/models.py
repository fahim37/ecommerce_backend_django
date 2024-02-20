from django.db import models

from core.utils import BaseModel
from product.models import Product


class Address(BaseModel):
    label = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)


class Review(BaseModel):
    rating = models.PositiveIntegerField()
    review = models.TextField(blank=True, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True, null=True
    )
