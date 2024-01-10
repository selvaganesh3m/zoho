from django.db import models
from apps.core.models import TimestampModel
from apps.product.models import Product


class Warehouse(TimestampModel):
    name = models.CharField(max_length=150, unique=True)
    location = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name


class WarehouseStock(TimestampModel):
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, related_name="warehouse_stocks"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="warehouse_stocks"
    )
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.warehouse.name} - {self.product.name} - {self.quantity}"
