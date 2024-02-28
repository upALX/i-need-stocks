import requests
from django.http import HttpResponseBadRequest
from requests.exceptions import HTTPError
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
        
        webhook_model = self.webhook_repository.create_webhook_model(
            webhook_url=webhook_url,
            stock_code=stock_code
        )

        webhook_dto = WebhookDTO(
            webhook_key=webhook_model.webhook_key,
            creation_date=webhook_model.created_at,
        )

        # print(f'The webhook dto created is {webhook_dto.__dict__}')

        return webhook_dto

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

            print(f'The response of sent webhook has the status {response.json()}')

            if response.status_code > 300:
                print('IS ON RAISE ERROR')
                raise HTTPError("On try sent the webhook occurs an error")
        except HTTPError as ex:
            return HttpResponseBadRequest("Bad request: " + str(ex))
        except Exception as ex:
            return Exception(str(ex))
        
        return
    