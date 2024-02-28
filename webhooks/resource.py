from django.http import JsonResponse, HttpRequest, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from .controller import WebhookController

@method_decorator(require_http_methods(["GET", "POST"]), name='dispatch')
class WebhookResource(View):
    '''
        receive all requests from webhooks
    '''

    def __init__(self) -> None:
        self.webhook_controller = WebhookController()

    @csrf_exempt
    def health_check_resource(self, request: HttpRequest):

        return HttpResponse()

    def post_create_webhooks(self, request: HttpRequest) -> None:
        '''
            receive and response all requests of stocks
        '''
        body_from_request = json.loads(request.body)

        print(f'The request body informed is {body_from_request}')

        webhook_dto = self.webhook_controller.create_webhook(
            request_body=body_from_request
        )

        return JsonResponse(webhook_dto.__dict__)
