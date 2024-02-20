from django.db import models

from orders.utils import BaseModel


class Address(BaseModel):
    label = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
