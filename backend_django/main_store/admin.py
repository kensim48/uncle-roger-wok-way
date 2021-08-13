from django.contrib import admin
from .models import *

# Register your models here.
class ItemListingAdmin(admin.ModelAdmin):
    fields = ["name", "price", "serial_id"]
    list_display = ("id", "name", "price", "serial_id")
    list_display_links = ("name",)

admin.site.register(ItemListing, ItemListingAdmin)

class ExtendUserAdmin(admin.ModelAdmin):
    fields = ["r", "is_admin"]
    list_display = ("r", "is_admin")

admin.site.register(ExtendUser, ExtendUserAdmin)