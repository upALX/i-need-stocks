from django.http import JsonResponse, HttpRequest, HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from .controller import StockController


@method_decorator(require_http_methods(["GET"]), name='dispatch')
class StockResource(View):
    '''
        All requests and responses of API
    '''

    def __init__(self) -> None:
        self.stock_controller = StockController()

    
    def get_health_check_resource(self, request: HttpRequest):
        

        return HttpResponse()

    def get_stocks(self, request: HttpRequest) -> None:
        '''
            receive and response all requests of stocks
        '''

        if request.method == 'GET':
            stock_code = request.GET.get('stock_code')

            if not stock_code:
                return JsonResponse({'error': 'stock_code query parameter is required'}, status=400)
            if len(stock_code) > 7:
                return JsonResponse({'error': 'Stock code must be at most 7 characters long.'}, status=400)

            print(f'The stock code is {stock_code}')

            stock_dto = self.stock_controller.get_stock_information(stock_code=stock_code.upper()) 

            return JsonResponse(stock_dto.__dict__)
        else:
            return JsonResponse({'error': 'This endpoint only accepts GET requests'}, status=405)
