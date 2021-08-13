from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class ItemListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemListing
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "is_staff"]
