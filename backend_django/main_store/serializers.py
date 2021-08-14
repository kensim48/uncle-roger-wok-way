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
        fields = ["id", "username", "email", "is_staff"]


class OrderItemSerializer(serializers.ModelSerializer):
    item = ItemListingSerializer(many=False, read_only=True)

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
