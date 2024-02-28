from .models import Stock

class StockRepository:
    '''
        All access to the stock table using repository pattern and django ORM
    '''
    
    def get_stock_by_key(self, stock_key: str) -> Stock:
        stock_model = Stock.objects.get(stock_key=stock_key)
        return stock_model

    def save_stock_information(self, stock_code: str, stock_data: dict):

        print(f'Is on save stock information with stock data {stock_data}')

        new_stock_model = Stock(stock_ticker_code=stock_code, stock_data=stock_data)

        print(f'The stock model is {new_stock_model}')
        
        new_stock_model.save()

        print(f'The model {new_stock_model} was saved on database.')

        return new_stock_model 