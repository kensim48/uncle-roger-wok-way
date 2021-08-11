from django.urls import path, re_path
from . import views

urlpatterns = [
    path("item_listings/", views.item_listing),
]
