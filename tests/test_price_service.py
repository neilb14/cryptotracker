import unittest, io
from unittest.mock import patch, MagicMock
from cryptotracker.price_service import PriceService

class TestGetPrice(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_get_price(self, mock_urlopen):
        cm = MagicMock()
        cm.getcode.return_value = 200
        cm.read.return_value = b'{"CAD":833.57}'
        cm.__enter__.return_value = cm
        mock_urlopen.return_value = cm
        service = PriceService()
        self.assertEqual(833.57, service.get_price('BTC'))

if __name__ == '__main__':
    unittest.main()