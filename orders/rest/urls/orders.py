from django.urls import path
from orders.rest.views.orders import OrderAPI

urlpatterns = [
    path("", OrderAPI.as_view()),
    path("<int:pk>/", OrderAPI.as_view()),
]
