import requests
from requests.exceptions import HTTPError, RequestException
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
        
        try:

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
        except Exception as ex:
            raise ex from None

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

                if counter <= MAX_RETRY:
                    http_response = requests.get(
                        headers=HEADERS,
                        url=base_url,
                        timeout=TIMEOUT,
                    )

                stock_data: dict = http_response.json()

                print(f'HAS STOCK DATA ERROR: {'Error Message' in stock_data}')

                print(f'THE STATUS CODE IS {http_response.status_code} and message is {http_response.json}')

                if counter > MAX_RETRY:
                    raise HTTPError("Max retry to get all information stock was exceeded.")
                if http_response.status_code == 200 and 'Information' in stock_data:
                    raise RequestException('The rate limit of requests per day has been reached.')
                if http_response.status_code == 200 and 'Error Message' not in stock_data:
                    break

                counter += 1

        except HTTPError as ex:
            print(f'The HTTP ERROR exception on get information is {str(ex)}')
            raise ex from None
        except RequestException as ex:
            print(f'The REQUEST EXCEPTION on get information is {str(ex)}')
            raise ex from None
        except Exception as ex:
            print(f'The exception on get information is {str(ex)}')
            raise ex from None

        return stock_data
    