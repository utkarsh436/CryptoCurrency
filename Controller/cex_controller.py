import requests
from util.utils import ErrorResponse

CEX_API = 'https://cex.io/api/ticker/%s/USD'

class CexService():
    def info(self, ticker):
        try:
           url = CEX_API % (ticker)

           response = requests.get(url=url)
           json_obj = eval(response.text)
           buy_amt = json_obj["bid"]
           sell_amt = json_obj["ask"]

           return {
               'buy': buy_amt,
               'sell': sell_amt,
           }

        except Exception as e:
            return ErrorResponse({'message': 'Internal Server Error'}, 500)
