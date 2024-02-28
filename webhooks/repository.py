from .models import Webhook
from django.core.exceptions import ObjectDoesNotExist

class WebhookRepository:
    '''
        All access to the webhook table using repository pattern and django ORM
    '''

    def create_webhook_model(
        self,
        stock_code: str,
        webhook_url: str
    ) -> Webhook:
        new_webhook_model = Webhook(stock_ticker_code= stock_code, webhook_url=webhook_url)

        print(f'Model of webhook created is {new_webhook_model.webhook_key}')

        new_webhook_model.save()

        print('Webhook model was saved')

        return new_webhook_model

    def get_webhook_by_stock_code(
        self,
        stock_code: str
    ) -> Webhook:

        try:
            webhook_model = Webhook.objects.get(
                stock_ticker_code=stock_code
            )

            print(f'On webhook repository the webhook model found with the stock code {stock_code} is {webhook_model}')

        except ObjectDoesNotExist:
            webhook_model = None
        
        return webhook_model

    def get_webhook_by_all(
        self,
        stock_code: str,
        webhook_url: str
    ) -> Webhook:
        try:

            print(f'Trying get the webhook with the code {stock_code} and url {webhook_url} on repository')
            
            webhook_model = Webhook.objects.get(
                stock_ticker_code=stock_code,
                webhook_url=webhook_url
            )

            print(f'On webhook repository the webhook model found with the stock code {stock_code} is {webhook_model}')

        except ObjectDoesNotExist:
            webhook_model = None
        
        return webhook_model