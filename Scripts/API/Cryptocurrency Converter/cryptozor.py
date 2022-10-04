import requests


class Cryptozor:
    def __init__(self, currency, cryptocurrency):
        self.currency = currency.upper()
        self.cryptocurrency = cryptocurrency.upper()

    def convert(self, amount):
        api = requests.get(
            "https://api.coinbase.com/v2/exchange-rates?currency="
            + self.cryptocurrency
        )
        try:
            currentPrice = api.json()["data"]["rates"][self.currency]
        except KeyError:
            pass
        # Bitcoin
        # if self.cryptocurrency == ('BTC'):
        operations = ["BTC", "ETH", "ETC", "BCH", "LTC", "ZEC", "ZRX"]
        if self.cryptocurrency in operations:
            return amount / float(currentPrice)
        return "Not Implemented"
