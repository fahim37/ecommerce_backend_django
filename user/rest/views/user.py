from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from user.renderer import UserRenderer
from user.rest.serializers.user import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserProfileSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


User = get_user_model()


# generate token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "Access Token": str(refresh.access_token),
        "Refresh Token": str(refresh),
    }


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response(
                {"token": token, "msg": "Registration Successfull"},
                status=status.HTTP_201_CREATED,
            )


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)

            if user is not None:
                token = get_tokens_for_user(user)
                return Response(
                    token,
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "errors": {
                            "non_field_errors": ["Email or password is not valid"]
                        }
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)
