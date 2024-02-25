from .models import Stock

class StockRepository:
    '''
        access database using repository pattern
    '''
    
    def get_stock_by_key(self, stock_key: str) -> Stock:
        stock_model = Stock.objects.get(stock_key=stock_key)
        return stock_model

   