import json
from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseNotAllowed
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from .controller import StockController

@method_decorator(require_http_methods(["GET"]), name='dispatch')
class StockResource(View):

    def __init__(self) -> None:
        self.stock_controller = StockController()

    
    def get_health_check_resource(self, request: HttpRequest):

        # response_check = self.stock_controller.health_check()

        return HttpResponse()

    def get_stocks(self, request: HttpRequest) -> None:
        '''
            receive and response all requests of stocks
        '''
        stock_code = request.GET.get('stock_code')

        print(f'The stock code is {stock_code}')

        stock_dto = self.stock_controller.get_stock_information(stock_code=stock_code) 

        return JsonResponse(stock_dto.__dict__)
