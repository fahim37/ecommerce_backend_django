from django.urls import path
from product.rest.views.category import CategoryAPI

urlpatterns = [
    path("", CategoryAPI.as_view()),
    path("<int:pk>/", CategoryAPI.as_view()),
]
