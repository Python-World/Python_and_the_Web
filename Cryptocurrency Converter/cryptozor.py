import requests

class Cryptozor:
    def __init__(self, currency, cryptocurrency):
        self.currency = currency.upper()
        self.cryptocurrency = cryptocurrency.upper()

    def convert(self, amount):
        api = requests.get('https://api.coinbase.com/v2/exchange-rates?currency='+self.cryptocurrency)
        try:
            currentPrice = api.json()['data']['rates'][self.currency]
        except KeyError:
            pass
        # Bitcoin
        if self.cryptocurrency == ('BTC'):
           return amount / float(currentPrice)
        # Ethereum
        elif self.cryptocurrency == ('ETH'):
            return amount / float(currentPrice)
        # Ethereum Classic
        elif self.cryptocurrency == ('ETC'):
            return amount / float(currentPrice)
        # Bitcoin Cash
        elif self.cryptocurrency == ('BCH'):
            return amount / float(currentPrice)
        # Litecoin
        elif self.cryptocurrency == ('LTC'):
            return amount / float(currentPrice)
        # ZCash
        elif self.cryptocurrency == ('ZEC'):
            return amount / float(currentPrice)
        # 0x
        elif self.cryptocurrency == ('ZRX'):
            return amount / float(currentPrice)
        else:
            print('The coin "'+self.cryptocurrency+'" isn\'t implemented yet or doesn\'t exist.')

