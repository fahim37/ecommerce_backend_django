from django.urls import path
from orders.rest.views.orders import OrderListView, OrderDetailView

urlpatterns = [
    path("", OrderListView.as_view()),
    path("<int:pk>/", OrderDetailView.as_view()),
]
