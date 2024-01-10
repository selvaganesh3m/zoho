from django.db import models
from apps.core.models import TimestampModel
from apps.product.models import Product


class SalesOrder(TimestampModel):
    ORDER_STATUS_CHOICES = (
        ("ORDER_RECIEVED","ORDER RECIEVED"),
        ("ORDER_PROCESSING", "ORDER PROCESSING"),
        ("ORDER_COMPLETED", "ORDER_COMPLETED"),
        ("INVOICE_ISSUED", "INVOICE ISSUED"),
    )
    status = models.CharField(
        max_length=30,
        choices=ORDER_STATUS_CHOICES,
        default="ORDER_RECIEVED",
    )
    customer = models.CharField(max_length=175)
    products = models.ManyToManyField(Product, related_name='sales_orders')
    invoice = models.FileField(upload_to='sales-invoices/',null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id}"



class ProductionOrder(TimestampModel):
    customer = models.CharField(max_length=175)
    products = models.ManyToManyField(Product, related_name='production_orders')
    is_from_sales_order = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    invoice = models.FileField(upload_to='production-invoices/', null=True, blank=True)
    

    def __str__(self) -> str:
        return f"{self.id}"
    
    