from django.urls import path

from product.rest.views.review import ReviewListView


urlpatterns = [
    path("", ReviewListView.as_view()),
]
