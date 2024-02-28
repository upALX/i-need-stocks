from django.http import JsonResponse, HttpRequest, HttpResponse
from rest_framework.exceptions import ValidationError
from django.views import View
import json
from .controller import WebhookController


class WebhookResource(View):
    '''
        receive all requests from webhooks
    '''

    def __init__(self) -> None:
        self.webhook_controller = WebhookController()

    def health_check_resource(self, request: HttpRequest):

        return HttpResponse(status=204)

    def post_create_webhooks(self, request: HttpRequest) -> None:
        '''
            receive and response all requests of stocks
        '''

        body_from_request = json.loads(request.body)

        stock_code: str = body_from_request.get('stock_code')
        webhook_url: str = body_from_request.get('webhook_url')

        if stock_code is not None and webhook_url is not None:

            try:

                print(f'{'http://' in webhook_url[0:7]}')

                if 'http://' not in webhook_url[0:7] and 'https://' not in webhook_url[0:8]:
                    raise ValidationError(f"The webhook url [{webhook_url}] needs to follow the standards of a URL.")
                if not stock_code.isalnum():
                    raise ValidationError({f'The stock code [{stock_code}] needs contain only string or numbers characters. Not special characters.'})
                
                print(f'The request body informed is {body_from_request}')

                webhook_dto = self.webhook_controller.create_webhook(
                    stock_code=stock_code,
                    webhook_url=webhook_url
                )

                return JsonResponse(webhook_dto.__dict__)
            except Exception as ex:
                return JsonResponse({'error_message': str(ex)}, status=400)
        else:
            return JsonResponse({'error': 'Invalid JSON format. Stock_code and webhook_url are required.'}, status=400)
