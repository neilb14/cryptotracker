import unittest
from cryptotracker.currencies import currency_factory

class TestCurrencyFactory(unittest.TestCase):
    def test_factory_creates_fiat(self):
        self.assertEqual('Fiat', currency_factory.create('CAD', 100).__class__.__name__)
        self.assertEqual('Fiat', currency_factory.create('USD', 100).__class__.__name__)
        self.assertEqual('Fiat', currency_factory.create('cad', 100).__class__.__name__)
        self.assertEqual('Fiat', currency_factory.create('usd', 100).__class__.__name__)

    def test_factory_creates_crypto(self):
        self.assertEqual('Crypto', currency_factory.create('BTC', 100).__class__.__name__)
        self.assertEqual('Crypto', currency_factory.create('btc', 100).__class__.__name__)
        self.assertEqual('Crypto', currency_factory.create('anything', 100).__class__.__name__)
        self.assertEqual('Crypto', currency_factory.create('XYZ', 100).__class__.__name__)

if __name__ == '__main__':
    unittest.main()