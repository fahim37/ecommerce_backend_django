from django.contrib import admin

from orders.models import Cart, Order, OrderProduct

# Register your models here.

from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderProduct)
