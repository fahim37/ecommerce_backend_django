from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from orders.models import Cart

from orders.rest.serializers.carts import CartSerializer


class CartListView(APIView):
    def post(self, request):
        serializer = CartSerializer(data=request.data)

        if serializer.is_valid():
            product = serializer.validated_data["product"]
            quantity = serializer.validated_data["quantity"]

            # Check if the product stock is sufficient
            if product.stock < quantity:
                return Response(
                    {"error": "Not enough stock available"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # If product already in cart, update the quantity
            cart = Cart.objects.filter(product=product).first()

            if cart:
                cart.quantity += quantity
                cart.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            # Save the cart
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartDetailView(APIView):
    def get(self, request, pk):
        pass
