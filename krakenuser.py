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
            price = ticker['b'][0]
            ratios[item] = float(price[:-5]) - float(orders[item]['price'])
        return ratios

    def get_balance_worth(self, in_name):
        balance = self.get_balance()
        keys = balance.keys()
        prices = {}
        for item in keys:
            name = self.market.assets[item]['altname']
            if name != in_name:
                balance_item = balance[item]
                ticker = self.market.get_ticker('{0}{1}'.format(name, in_name))
                amount = float(balance_item) * float(ticker['b'][0][:-5])
                prices[name] = amount
        return prices
