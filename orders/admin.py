from django.contrib import admin

from .models import Cart, Order, OrderProduct, Transaction

admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Transaction)
