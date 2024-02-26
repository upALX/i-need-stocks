from .models import Webhook

class WebhookRepository:
    '''
        access database using repository pattern
    '''
    
    def create_webhook_model(self, stock_key: str) -> Webhook:
        pass
   