from django.db import models
from orders.utils import BaseModel


class Order(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    shipping_address = models.CharField(max_length=255, blank=True, null=True)
    order_status = models.CharField(max_length=255, blank=True, null=True)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="items", blank=True, null=True
    )
    product_id = models.IntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
