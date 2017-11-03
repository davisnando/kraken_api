""" kraken user class"""
from krakenmarket import KrakenMarket

class KrakenUser:
    def __init__(self, krakenapi):
        self.api = krakenapi
        self.market = KrakenMarket(self.api)

    def get_balance(self):
        """ Get account balance  """
        result = self.api.private_request("/0/private/Balance", {})
        self.balance = result
        return result['result']

    def get_orders(self):
        """ Get closed orders """
        result = self.api.private_request("/0/private/ClosedOrders", {})
        return result['result']['closed']

    def get_ratios(self):
        """ Get ratio of your orders based on current price """
        orders = self.get_orders()
        keys = orders.keys()
        ratios = {}
        for item in keys:
            pair = orders[item]['descr']['pair']
            ticker = self.market.get_ticker(pair)
            ticker_key = list(ticker['result'].keys())
            price = ticker['result'][ticker_key[0]]['b'][0]
            ratios[item] = float(price[:-5]) - float(orders[item]['price'])
        return ratios
