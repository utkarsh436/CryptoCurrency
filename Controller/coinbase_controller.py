import requests
from util.utils import ErrorResponse

COINBASE_API = 'https://api.coinbase.com/v2/prices/%s-USD/%s'

class CoinBaseService():
    def info(self, ticker):
        try:
           buy_url = COINBASE_API % (ticker, 'buy')
           sell_url = COINBASE_API % (ticker, 'sell')

           buy_response = requests.get(url=buy_url)
           buy_json_obj = eval(buy_response.text)
           buy_amt = buy_json_obj["data"]["amount"]

           sell_response = requests.get(url=sell_url)
           sell_json_obj = eval(sell_response.text)
           sell_amt = sell_json_obj["data"]["amount"]

           return {
               'buy': buy_amt,
               'sell': sell_amt,
           }

        except Exception as e:
            return ErrorResponse({'message': 'Internal Server Error'}, 500)
