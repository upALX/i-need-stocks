from django.urls import path
from .resource import WebhookResource

webhook_resource = WebhookResource()

urlpatterns = [
    path('webhook_health/', webhook_resource.health_check_resource, name='health_check_resource'),
    path('webhook/subscribe/', webhook_resource.post_create_webhooks, name='post_create_webhooks'),
]