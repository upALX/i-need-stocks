from .dto.webhook_dto import WebhookDTO
from .repository import WebhookRepository

class WebhookController:

    def __init__(self) -> None:
        self.webhook_repository = WebhookRepository

    def create_webhook(self, request_body: dict) -> WebhookDTO:
        
        stock_code = request_body.get('stock_code')
        webhook_url = request_body.get('webhook_url')

        print(f'Request body received on CONTROLLER {request_body}')

        webhook_model = self.webhook_repository.create_webhook_model(
            self, 
            webhook_url=webhook_url, 
            stock_code=stock_code
        )

        webhook_dto = WebhookDTO(
            webhook_key=webhook_model.webhook_key,
            creation_date=webhook_model.created_at,
        )

        return webhook_dto