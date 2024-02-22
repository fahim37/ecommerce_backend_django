from django.urls import path, include

urlpatterns = [
    path("", include("user.rest.urls.user")),
]
