from django.db import models

from product.utils import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
