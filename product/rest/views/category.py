from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product.models import Category
from product.rest.serializers.products import CategorySerializer


class ProductAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            category = Category.objects.get(id=id)
            serializer = CategorySerializer(category)
            return Response(serializer.data)

        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Category Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Category Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        category = Category.objects.get(id=id)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Partial Category Updated"})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        category = Category.objects.get(id=id)
        category.delete()
        return Response({"msg": "Category Deleted"})
