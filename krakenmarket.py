class KrakenMarket:
    def __init__(self, krakenAPI):
        self.api = krakenAPI
        self.assets = self.get_assets()
    def get_ticker(self, pair):
        return self.api.public_request('/0/public/Ticker', {'pair': pair})

    def get_assets(self):
        return self.api.public_request('/0/public/Assets', {})

    def get_spread_data(self, pair):
        return self.api.public_request('/0/public/Spread', {'pair': pair})
