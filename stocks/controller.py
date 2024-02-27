import requests
from werkzeug.exceptions import BadRequest
from .dto.stock_dto import StockDTO
from .repository import StockRepository
from webhooks.controller import WebhookController
from .constants import MAX_RETRY, API_KEY_V1, API_KEY_V2

class StockController:

    def __init__(self) -> None:
        self.headers = {'Content-Type': 'application/json'}
        self.stock_repository = StockRepository()
        self.webhook_controller = WebhookController()

    def get_stock_information(self, stock_code: str) -> StockDTO:
        counter = 0
        base_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_code}&interval=5min&apikey={API_KEY_V1}'
        stock_model = None

        webhook_model = self.webhook_controller.get_webhook_by_stock_code(
            stock_code=stock_code
        )

        try:
            while True:
                print(f'The counter requests is {counter}')
                stock_data = requests.get(headers=self.headers, url=base_url)

                json_data_response = stock_data.json()

                if stock_data.status_code < 300:

                    print(f'The stock data catch is {stock_data.json}')

                    stock_model = self.stock_repository.save_stock_information(
                        stock_code=stock_code,
                        stock_data=json_data_response
                    )

                    if webhook_model is not None:
                        print('ON SENT WEBHOOK')
                        self.webhook_controller.sent_webhook(
                            stock_code=stock_code,
                            stock_key=stock_model.stock_key,
                            webhook_url=webhook_model.webhook_url,
                            stock_data=json_data_response
                        )

                        print('WEBHOOK SENT!')

                    break

                if counter == MAX_RETRY:
                    raise BadRequest('Max retry to get all information stock was exceeded.')

                
                counter += 1

        except BadRequest as ex:
            return BadRequest(f'Bad request: {str(ex)}')
        
        except Exception as ex:
            return Exception(str(ex))
        
        stock_dto = StockDTO(
            stock_key=stock_model.stock_key,
            stock_data=stock_model.stock_data
        )

        return stock_dto
    