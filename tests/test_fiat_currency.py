import unittest
from cryptotracker.currencies import fiat

class TestFiatCurrency(unittest.TestCase):
    def test_is_fiat_should_recognize_fiat_currencies(self):
        self.assertTrue(fiat.is_fiat('CAD'))
        self.assertTrue(fiat.is_fiat('USD'))
        self.assertTrue(fiat.is_fiat('cad'))
        self.assertTrue(fiat.is_fiat('usd'))

    def test_is_fiat_should_recognize_non_fiat_currencies(self):
        self.assertFalse(fiat.is_fiat('BTC'))
        self.assertFalse(fiat.is_fiat('btc'))
        self.assertFalse(fiat.is_fiat('anything'))
        self.assertFalse(fiat.is_fiat('XYZ'))

if __name__ == '__main__':
    unittest.main()