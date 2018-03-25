import unittest
from cryptotracker import cli

class TestCommandLineArgs(unittest.TestCase):
    def test_default_arguments(self):
        result = cli.parse_args('--amount 0.1 --rate 1192'.split())
        self.assertEqual('CAD', result.from_currency)
        self.assertEqual('BTC', result.to_currency)
        self.assertEqual(0, result.charge)

if __name__ == '__main__':
    unittest.main()