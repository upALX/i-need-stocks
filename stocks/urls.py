from django.urls import path
from .resource import StockResource

stock_resource = StockResource()

urlpatterns = [
    path(route='stocks_health/', view=stock_resource.get_health_check_resource, name='get_health_check_resource'),
    path(route='stock/', view=stock_resource.get_stocks, name='get_stocks'),
]