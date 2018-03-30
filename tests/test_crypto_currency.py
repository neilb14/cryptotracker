import unittest
from cryptotracker.currencies.crypto import Crypto

class TestCryptoCurrency(unittest.TestCase):
    def test_fiat_write(self):
        self.assertEqual('100.000000', str(Crypto(100)))
        self.assertEqual('9.123457', str(Crypto(9.1234567)))
        
if __name__ == '__main__':
    unittest.main()