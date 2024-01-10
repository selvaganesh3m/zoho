from django.db import models
from apps.core.models import TimestampModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Customer(TimestampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customers')
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name