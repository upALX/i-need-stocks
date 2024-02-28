import requests
from requests.exceptions import HTTPError
from django.core.exceptions import BadRequest
from constants import HEADERS, TIMEOUT
from .dto.webhook_dto import WebhookDTO
from .models import Webhook
from .repository import WebhookRepository

class WebhookController:
    '''
        All Webhook algorithm logics 
    '''

    def __init__(self) -> None:
        self.webhook_repository = WebhookRepository()

    def create_webhook(
        self,
        stock_code: str,
        webhook_url: str,
    ) -> WebhookDTO:
        
        try:

            webhook_already_exists = self.get_webhook_by_all(
                stock_code=stock_code,
                webhook_url=webhook_url
            )

            print(f'The webhook model already exists: {webhook_already_exists}')

            if webhook_already_exists is not None:
                raise BadRequest(f'Already exists an webhook register with the stock {stock_code} and url {webhook_url}')
        
            webhook_model = self.webhook_repository.create_webhook_model(
                webhook_url=webhook_url,
                stock_code=stock_code
            )

            webhook_dto = WebhookDTO(
                webhook_key=webhook_model.webhook_key,
                creation_date=webhook_model.created_at,
            )

        except Exception as ex:
            raise ex from None
        # print(f'The webhook dto created is {webhook_dto.__dict__}')

        return webhook_dto
    
    def get_webhook_by_all(
        self,
        stock_code: str,
        webhook_url: str
    ) -> Webhook:
        print('Trying get the webhook')

        webhook_model = self.webhook_repository.get_webhook_by_all(
            stock_code=stock_code,
            webhook_url=webhook_url
        )

        print(f'The webhook getted on Webhook module is {webhook_model}')

        return webhook_model
    
    def get_webhook_by_stock_code(
        self,
        stock_code: str
    ) -> Webhook:

        webhook_model = self.webhook_repository.get_webhook_by_stock_code(
            stock_code=stock_code,
        )

        return webhook_model
    
    def sent_webhook(
        self,
        stock_code: str,
        stock_key: str,
        webhook_url: str,
        stock_data,
    ) -> None:
        
        try:
            print(f'trying sent the stock {stock_key} to url {webhook_url}')

            json_data = {
                "symbol": f'{stock_code}',
                "stock_key": f'{stock_key}',
                "stock_data": f'{stock_data}'
            }
            
            print(f'The JSON data to send is {json_data}')

            response = requests.post(
                url=webhook_url,
                headers=HEADERS,
                json=json_data,
                timeout=TIMEOUT
            )

            print(f'The response of sent webhook has the status {response.content}')

            if response.status_code > 300:
                raise HTTPError("On try sent the webhook occurs an error")
        except HTTPError as ex:
            raise ex from None
        except Exception as ex:
            raise ex from None
        
        return
    