from django.contrib import admin
from .models import *

# Register your models here.


class ItemListingAdmin(admin.ModelAdmin):
    fields = ["name", "price", "serial_id"]
    list_display = ("id", "name", "price", "serial_id")
    list_display_links = ("name",)


admin.site.register(ItemListing, ItemListingAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    fields = ["item", "quantity"]
    list_display = ("item", "quantity")


admin.site.register(OrderItem, OrderItemAdmin)


class OrderAdmin(admin.ModelAdmin):
    fields = ["items", "user"]
    list_display = ("user",)


admin.site.register(Order, OrderAdmin)
