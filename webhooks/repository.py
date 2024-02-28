from .models import Webhook

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

        webhook_model = Webhook.objects.get(
            stock_ticker_code=stock_code
        )

        print(f'On webhook repository the webhook model found with the stock code {stock_code} is {webhook_model}')

        return webhook_model
