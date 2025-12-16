from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ("product", "quantity", "price_per_unit", "total_price")
    readonly_fields = ("price_per_unit", "total_price")
    extra = 0

    def price_per_unit(self, obj):
        return obj.product.price


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = (
        "id",
        "user",
        "created_at",
        "updated_at",
        "total_price",
        "item_count",
    )

    def item_count(self, obj):
        return obj.items.count()
