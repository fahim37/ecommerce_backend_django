from django.urls import path

from user.rest.views import UserRegistrationView

urlpatterns = [path("register/", UserRegistrationView.as_view(), name="registration")]
