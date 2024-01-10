from django.contrib import admin
from .models import SalesOrder, ProductionOrder


class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "status")
    list_filter = ("status",)


class ProductionOrderAdmin(admin.ModelAdmin):
    list_display = ("customer","is_from_sales_order", "is_completed")
    list_filter = ("is_from_sales_order", "is_completed")
    list_editable = ("is_completed",)



admin.site.register(SalesOrder, SalesOrderAdmin)
admin.site.register(ProductionOrder, ProductionOrderAdmin)