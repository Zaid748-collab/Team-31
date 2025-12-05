from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "quantity_in_stock",
        "reorder_point",
        "active",
        "type",
    )
    search_fields = ("name", "description", "type")
    list_filter = ("active", "type")