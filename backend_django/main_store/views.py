from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# Create your views here.
@api_view(["GET"])
def item_listing(request):
    if request.method == "GET":
        id = request.query_params.get("id", None)
        item_listings = ItemListing.objects.all()
        if id is not None:
            item_listings = item_listings.filter(id=id)
        if len(item_listings) == 0:
            return JsonResponse({}, status=404)
        serializer = ItemListingSerializer(item_listings, many=True)
        return JsonResponse({"data": serializer.data}, safe=False)
