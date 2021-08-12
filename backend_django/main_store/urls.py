from django.urls import path, re_path
from . import views

urlpatterns = [
    path("item_listing/", views.item_listing),
    path("item_modify/", views.item_modify),
]
