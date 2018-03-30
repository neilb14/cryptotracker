import unittest
from cryptotracker.currencies.fiat import Fiat

class TestFiatCurrency(unittest.TestCase):
    def test_fiat_write(self):
        self.assertEqual('$100.00', str(Fiat(100)))
        self.assertEqual('$9.12', str(Fiat(9.1234567)))
        self.assertEqual('$9.79', str(Fiat(9.789)))
        
if __name__ == '__main__':
    unittest.main()