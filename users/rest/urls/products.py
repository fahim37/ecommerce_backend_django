from django.urls import path
from product.rest.views.products import ProductAPI

urlpatterns = [
    path("", ProductAPI.as_view()),
    path("<int:pk>/", ProductAPI.as_view()),
]
