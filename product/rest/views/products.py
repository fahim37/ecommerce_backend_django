from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from product.rest.serializers.products import ProductSerializer


class ProductListView(APIView):
    def get(self, request, pk=None, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"msg": "Product Created", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    def get(self, request, pk, format=None):
        id = pk
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise NotFound()

        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        id = pk
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise NotFound()

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Product Updated", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise NotFound()

        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Partial Product Updated", "data": serializer.data})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise NotFound()

        product.delete()
        return Response({"msg": "Product Deleted", "data": []})
