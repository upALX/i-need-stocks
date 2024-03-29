import uuid
from django.db import models


class Stock(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    stock_key = models.UUIDField(default=uuid.uuid4, editable=False, null=False)
    stock_ticker_code = models.CharField(max_length=7, null=False)
    stock_data = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    objects = models.Manager()
