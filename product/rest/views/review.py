from rest_framework.views import APIView
from rest_framework.response import Response

from product.rest.serializers.review import ReviewSerializer


class ReviewListView(APIView):

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
