import unittest
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

if __name__ == '__main__':
    unittest.main()