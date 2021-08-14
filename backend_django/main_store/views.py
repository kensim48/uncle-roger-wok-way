import enum
from re import T
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


@api_view(["GET"])
def item_listing(request):
    if request.method == "GET":
        id = request.query_params.get("item_id", None)
        item_listings = ItemListing.objects.all()
        if id is not None:
            item_listings = item_listings.filter(id=id)
        if len(item_listings) == 0:
            return JsonResponse({}, status=404)
        serializer = ItemListingSerializer(item_listings, many=True)
        return JsonResponse({"data": serializer.data})


@api_view(["POST", "DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def item_modify(request):
    # Only for staff
    if not request.user.is_staff:
        return JsonResponse({}, status=403)
    # For both creating and modifying
    if request.method == "POST":
        data = JSONParser().parse(request)
        if "id" in data:
            id = data["id"]
            item_listing = get_object_or_404(ItemListing, id=id)
            serializer = ItemListingSerializer(item_listing, data=data)
            statuscode = 200
        else:
            serializer = ItemListingSerializer(data=data)
            statuscode = 201
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=statuscode)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        data = JSONParser().parse(request)
        if "id" in data:
            id = data["id"]
            item_listing = get_object_or_404(ItemListing, id=id)
            if item_listing is not None:
                item_listing.delete()
                return JsonResponse({}, status=200)
        return JsonResponse({}, status=400)


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def send_order(request):
    if request.method == "POST":
        order_items_dict = JSONParser().parse(request)["data"]
        order_item_ids = [x["id"] for x in order_items_dict]
        items = ItemListing.objects.filter(id__in=order_item_ids)
        order_items = []
        for count, item in enumerate(items):
            order_items.append(
                OrderItem(item=item, quantity=order_items_dict[count]["quantity"])
            )
        OrderItem.objects.bulk_create(order_items)
        order = Order(user=request.user)
        order.save()
        order.items.add(*order_items)
        order.save()
        return JsonResponse({}, status=200)


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def view_order(request):
    if request.method == "GET":
        # Only for staff
        if not request.user.is_staff:
            return JsonResponse({}, status=403)
        orders = Order.objects.all()
        user_id = request.query_params.get("user_id", None)
        if user_id is not None:
            orders = orders.filter(user__id=user_id)
        # Booking id
        id = request.query_params.get("booking_id", None)
        if id is not None:
            orders = orders.filter(id=id)
        if len(orders) == 0:
            return JsonResponse({}, status=404)
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse({"data": serializer.data}, status=200)


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def whoami(request):
    if request.method == "GET":
        serializer = UserSerializer(request.user, many=False)
        return JsonResponse(serializer.data)
