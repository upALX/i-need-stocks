from django.http import HttpResponseBadRequest
import requests
from requests.exceptions import HTTPError
from webhooks.controller import WebhookController
from constants import MAX_RETRY, API_KEY_V1, HEADERS, TIMEOUT
from .dto.stock_dto import StockDTO
from .repository import StockRepository


class StockController:
    '''
        Here is all algorithm logic about stocks
    '''

    def __init__(self) -> None:
        self.stock_repository = StockRepository()
        self.webhook_controller = WebhookController()

    def get_stock_information(
        self, 
        stock_code: str
    ) -> StockDTO:

        stock_data = self.get_stock_information_by_stock_code(
            stock_code=stock_code,
        )

        stock_model = self.stock_repository.save_stock_information(
            stock_code=stock_code,
            stock_data=stock_data
        )

        webhook_model = self.webhook_controller.get_webhook_by_stock_code(
            stock_code=stock_code
        )

        if webhook_model is not None:
            self.webhook_controller.sent_webhook(
                stock_code=stock_code,
                stock_key=stock_model.stock_key,
                webhook_url=webhook_model.webhook_url,
                stock_data=stock_data
            )

        stock_dto = StockDTO(
            stock_key=stock_model.stock_key,
            stock_data=stock_model.stock_data
        )

        return stock_dto
    
    def get_stock_information_by_stock_code(
        self,
        stock_code: str,
    ) -> dict:
        counter = 0
        base_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_code}&interval=5min&apikey={API_KEY_V1}'

        try:
            while True:
                print(f'The counter requests is {counter}')
                
                http_response = requests.get(
                    headers=HEADERS,
                    url=base_url,
                    timeout=TIMEOUT,
                )

                print(f'THE STATUS CODE IS {http_response.status_code} and message is {http_response.json}')

                if counter == MAX_RETRY:
                    raise HTTPError("Max retry to get all information stock was exceeded.")

                if http_response.status_code == 200:
                    stock_data: dict = http_response.json()
                    return stock_data

                counter += 1
        
        except HTTPError as ex:
            return HttpResponseBadRequest("Bad request: " + str(ex))
        except Exception as ex:
            return Exception(str(ex))
