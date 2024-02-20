from decimal import Decimal
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers import AddressSerializer
from orders.models import Cart, Order, OrderProduct, Transaction
from orders.rest.serializers.orders import OrderSerializer


class OrderListView(APIView):
    def get(self, request, pk=None, format=None):

        try:
            orders = Order.objects.all()
        except Order.DoesNotExist:
            return Response(
                {"message": "No orders found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            cart_products = Cart.objects.all()
            total_price = Decimal(0)

            if not cart_products:
                return Response(
                    {"message": "No products in cart"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            for cart in cart_products:
                OrderProduct.objects.create(
                    product=cart.product,
                    quantity=cart.quantity,
                    order=serializer.save(),
                )
                # calculate the total price checking discount
                total_price += (
                    cart.product.price
                    * cart.quantity
                    * (1 - cart.product.discount / 100)
                )
                cart.delete()

            Transaction.objects.create(
                amount=total_price, status="Paid", order=serializer.save()
            )

            serializer.validated_data["order_price"] = total_price

            address_data = request.data.get("address", {})
            address_serializer = AddressSerializer(data=address_data)

            # Validate and create the address instance
            if address_serializer.is_valid():
                address_instance = address_serializer.save()

            serializer.save(address=address_instance, **serializer.validated_data)

            return Response(
                {"message": "Order created"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(APIView):
    def get(self, request, pk, format=None):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response(
                {"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response(
                {"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Order updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response(
                {"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Order partially updated"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response(
                {"message": "Order not found"}, status=status.HTTP_404_NOT_FOUND
            )
        order.delete()
        return Response({"message": "Order deleted"}, status=status.HTTP_204_NO_CONTENT)
