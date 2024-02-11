from django.db import models
from product.utils import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)


class Product(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(
        "Image",
        upload_to="images/testimagemodel/",
        width_field="width",
        height_field="height",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, blank=True, null=True
    )
