from re import T
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

# Create your views here.
@api_view(["GET", "POST"])
def item_listing(request):
    if request.method == "GET":
        id = request.query_params.get("id", None)
        item_listings = ItemListing.objects.all()
        if id is not None:
            item_listings = item_listings.filter(id=id)
        if len(item_listings) == 0:
            return JsonResponse({}, status=404)
        serializer = ItemListingSerializer(item_listings, many=True)
        return JsonResponse({"data": serializer.data})
    
    # For both creating and modifying
    elif request.method == "POST":
        data = JSONParser().parse(request)
        if "id" in data:
            id = data["id"]
            item_listing = ItemListing.objects.get(id=id)
            serializer = ItemListingSerializer(item_listing, data=data)
            statuscode = 200
        else:
            serializer = ItemListingSerializer(data=data)
            statuscode = 201
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=statuscode)
        return JsonResponse(serializer.errors, status=400)
