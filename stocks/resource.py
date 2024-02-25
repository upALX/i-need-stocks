from django.http import JsonResponse, HttpRequest, HttpResponse
from .controller import StockController
from rest_framework import viewsets
from stocks.models import Stock

# Create your views here.
class StockResource:

    # def __init__(self) -> None:
    #     self.stock_controller = StockController()

    
    def health_check_resource(self, request: HttpRequest):

        # response_check = self.stock_controller.health_check()

        return HttpResponse('OK')


    def stocks(self, request: HttpRequest) -> None:
        '''
            receive and response all requests of stocks
        '''
        
        return
