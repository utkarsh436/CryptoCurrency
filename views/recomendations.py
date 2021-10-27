from builtins import Exception, staticmethod
from flask import request
from flask_restful import Resource

from Controller.cex_controller import CexService
from Controller.coinbase_controller import CoinBaseService
from util.utils import ErrorResponse, buy, sell


class Recomendations(Resource):
    @staticmethod
    def get():
        try:
            coinbase_service = CoinBaseService()
            cex_service = CexService()
            args_list = request.args or {}
            if not args_list:
                # no ticker query param was passed throw exception
                raise Exception({'message': 'Invalid Request'}, 400)
            ticker = args_list.get('ticker')
            coinbase_info = coinbase_service.info(ticker)
            cex_info = cex_service.info(ticker)
            best_buy_info = buy(coinbase_info['buy'], 'coinbase', cex_info['buy'], 'cex')
            best_sell_info = sell(coinbase_info['sell'],'coinbase', cex_info['sell'], 'cex')

            result = {
                    'coinbase': coinbase_info,
                    'cex': cex_info,
                    'best_buy_info': best_buy_info,
                    'best_sell_info': best_sell_info
            }

            return result
        except Exception as e:
            return ErrorResponse({'message': 'Internal Server Error'}, 500)

