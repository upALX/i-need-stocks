import requests
from django.http import JsonResponse
from werkzeug.exceptions import BadRequest
from .dto.stock_dto import StockDTO
from .repository import StockRepository
from .constants import MAX_RETRY, API_KEY

class StockController:

    def __init__(self) -> None:
        self.stock_repository = StockRepository()

    def get_stock_information(self, stock_code: str) -> StockDTO:
        counter = 0
        headers = {'Content-Type': 'application/json'}
        base_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_code}&interval=5min&apikey={API_KEY}'
        stock_model = None

        try:
            while True:
                stock_data = requests.get(headers=headers, url=base_url)

                if stock_data.status_code < 300:
                    stock_model = self.stock_repository.save_stock_information(
                        stock_code=stock_code,
                        stock_data=stock_data
                    )

                    break

                if counter == MAX_RETRY:
                    raise BadRequest('Max retry to get all information stock was exceeded.')

                counter += 1

        except BadRequest as ex:
            return JsonResponse({'error': str(ex)}, status=400)
        
        stock_dto = StockDTO(
            stock_key=stock_model.stock_key,
            stock_data=stock_model.stock_data
        )

        return stock_dto
    