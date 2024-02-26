from django.urls import path
from .resource import StockResource

stock = StockResource()

urlpatterns = [
    path('health/', stock.health_check_resource, name='health_check_resource'),
]