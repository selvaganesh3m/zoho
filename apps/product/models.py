from django.db import models
from apps.core.models import TimestampModel



class Product(TimestampModel):
    name = models.CharField(max_length=75)
    sku = models.CharField(max_length=15, unique=True)
    price = models.PositiveSmallIntegerField()
    discounted_price = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.name
    


