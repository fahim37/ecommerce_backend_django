from django.urls import path

from user.rest.views.user import UserRegistrationView


urlpatterns = [path("register/", UserRegistrationView.as_view(), name="registration")]
