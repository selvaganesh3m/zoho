from django.contrib import admin
from .models import Product




class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'price', 'discounted_price')

admin.site.register(Product, ProductAdmin)
