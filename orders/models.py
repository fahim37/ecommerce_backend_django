from django.db import models
from core.models import Address
from core.utils import BaseModel
from product.models import Product


class Order(BaseModel):
    order_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    delivery_date = models.DateField(blank=True, null=True)
    address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, blank=True, null=True
    )
    status = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total_price = self.order_price + self.delivery_charge
        super().save(*args, **kwargs)


class OrderProduct(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True, null=True
    )
    selling_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    quantity = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.selling_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

        order = self.order
        order.order_price = sum(
            item.selling_price for item in order.orderproduct_set.all()
        )
        order.save()

        product = self.product
        product.stock -= self.quantity

        product.save()


class Cart(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, blank=True, null=True
    )
    quantity = models.PositiveIntegerField(blank=True, null=True)


class Transaction(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=255, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
