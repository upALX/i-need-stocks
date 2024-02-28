import uuid
from django.db import models

class Webhook(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    webhook_key = models.UUIDField(default=uuid.uuid4, editable=False, null=False)
    stock_ticker_code = models.CharField(max_length=7, null=False)
    webhook_url = models.CharField(max_length=700, null=False)
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    objects = models.Manager()
