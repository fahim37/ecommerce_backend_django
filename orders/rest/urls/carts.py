from django.urls import path
from orders.rest.views.carts import CartListView, CartDetailView

urlpatterns = [
    path("", CartListView.as_view()),
    path("<int:pk>/", CartDetailView.as_view()),
]
