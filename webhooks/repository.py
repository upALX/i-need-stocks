from .models import Webhook

class WebhookRepository:
    '''
        access database using repository pattern
    '''
    def create_webhook_model(self, stock_code: str, webhook_url: str) -> Webhook:
        new_webhook_model = Webhook(stock_ticker_code= stock_code, webhook_url=webhook_url)

        print(f'Model of webhook created is {new_webhook_model.webhook_key}')

        new_webhook_model.save()
        
        print('Webhook model was saved')

        return new_webhook_model
   