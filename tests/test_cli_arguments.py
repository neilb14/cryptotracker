import unittest
from datetime import datetime
from cryptotracker import cli

class TestCommandLineArgs(unittest.TestCase):
    def test_default_arguments(self):
        result = cli.parse_args('--amount 0.1 --rate 1192'.split())
        self.assertEqual('CAD', result['from_currency'])
        self.assertEqual('BTC', result['to_currency'])
        self.assertEqual(0, result['charge'])

    def test_from_currency(self):
        result = cli.parse_args('--from USD --amount 0.1 --rate 1192'.split())
        self.assertEqual('USD', result['from_currency'])

    def test_to_currency(self):
        result = cli.parse_args('--to ETH --amount 0.1 --rate 665'.split())
        self.assertEqual('ETH', result['to_currency'])

    def test_default_date(self):
        result = cli.parse_args('--amount 0.1 --rate 1192'.split())
        self.assertEqual(datetime.now().strftime('%Y%m%d'), result['date'].strftime('%Y%m%d'))

    def test_info(self):
        result = cli.parse_args(['-i'])
        self.assertTrue(result['info'])

if __name__ == '__main__':
    unittest.main()