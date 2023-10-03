from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("bussiness/", views.bussiness),
    path("entertainment/", views.entertainment),
    path("sports/", views.sports),
]
