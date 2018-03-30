from cryptotracker.currencies.fiat import Fiat
from cryptotracker.currencies.crypto import Crypto

def create(currency, value):
    if currency.upper() in ['CAD', 'USD']:
        return Fiat(value)
    else:
        return Crypto(value)

