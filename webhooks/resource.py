from django.http import HttpRequest, HttpResponse
from .controller import WebhookController

class WebhookResource:
    '''
        receive all requests from webhooks
    '''

    def __init__(self) -> None:
        self.webhook_controller = WebhookController()

    
    def health_check_resource(self, request: HttpRequest):
        '''
            verify if the webhook module is running...
        '''

        # response_check = self.stock_controller.health_check()

        return HttpResponse('OK')


    def webhooks(self, request: HttpRequest) -> None:
        '''
            receive and response all requests of stocks
        '''
        return
