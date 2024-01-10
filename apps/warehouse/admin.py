from django.contrib import admin
from .models import Warehouse, WarehouseStock




class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    list_filter = ('location',)

class WarehouseStockAdmin(admin.ModelAdmin):
    list_display = ('warehouse', 'product', 'quantity')
    list_filter = ('warehouse', 'product')


admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(WarehouseStock, WarehouseStockAdmin)

