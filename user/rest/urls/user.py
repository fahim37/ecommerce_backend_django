from django.urls import path

from user.rest.views.user import UserRegistrationView, UserLoginView, UserProfileView


urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="registration"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
]
