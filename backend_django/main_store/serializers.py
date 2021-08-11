from rest_framework import serializers
from .models import *


class ItemListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemListing
        fields = "__all__"
