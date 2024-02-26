from .models import Stock

class StockRepository:
    '''
        access database using repository pattern
    '''
    
    def get_stock_by_key(self, stock_key: str) -> Stock:
        stock_model = Stock.objects.get(stock_key=stock_key)
        return stock_model

    def save_stock_information(self, stock_code: str, stock_data: dict or any):

        new_stock_model = Stock(stock_ticker_code=stock_code, stock_data=stock_data)
        
        new_stock_model.save()

        return new_stock_model 