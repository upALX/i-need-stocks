from django.http import JsonResponse, HttpRequest, HttpResponse
from django.views import View
from rest_framework.exceptions import ValidationError
from .controller import StockController


class StockResource(View):
    '''
        All requests and responses of API
    '''

    def __init__(self) -> None:
        self.stock_controller = StockController()

    
    def get_health_check_resource(self, request: HttpRequest):
        

        return HttpResponse(status=204)

    def get_stocks(self, request: HttpRequest) -> None:
        '''
            receive and response all requests of stocks
        '''

        if request.method == 'GET':
            try:
                stock_code = request.GET.get('stock_code')

                if not stock_code:
                    raise ValidationError({'error': 'stock_code query parameter is required'})
                if len(stock_code) > 7:
                    raise ValidationError({'error': 'Stock code must be at most 7 characters long.'})
                if not stock_code.isalnum():
                    raise ValidationError({'error': 'stock_code query parameter is required'})

                print(f'The stock code is {stock_code}')

                stock_dto = self.stock_controller.get_stock_information(stock_code=stock_code.upper())

                return JsonResponse(stock_dto.__dict__)
            except Exception as ex:
                return JsonResponse({'error_message': str(ex)}, status=400)
        else:
            return JsonResponse({'error': 'This endpoint only accepts GET requests'}, status=405)
