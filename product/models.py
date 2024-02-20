from django.db import models
from django.utils.text import slugify

from product.utils import BaseModel

from versatileimagefield.fields import VersatileImageField


class Category(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField(default=0)
    image = VersatileImageField(
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, blank=True, null=True
    )
