import unittest, io
from datetime import datetime
from cryptotracker import summary_writer

class TestDatastore(unittest.TestCase):
    def test_headers_are_in_summary(self):
        summary = {}
        results = summary_writer.write(summary)
        self.assertEqual(1, len(results))
        self.assertTrue('Coin' in results[0])
        self.assertTrue('Amount' in results[0])
        self.assertTrue('Fees' in results[0])

    def test_summary_string_for_single_coin(self):
        summary = {'BTC':{'amount':100,'fees':1}}
        results = summary_writer.write(summary)
        self.assertEqual(2, len(results))
        self.assertTrue('BTC' in results[1])
        self.assertTrue('100' in results[1])

    def test_summary_string_rounding(self):
        summary = {'BTC':{'amount':100.23456789,'fees':0.00123456789012345}}
        results = summary_writer.write(summary)
        self.assertEqual(2, len(results))
        self.assertTrue('BTC' in results[1])
        self.assertTrue('100.234568' in results[1])
        self.assertTrue('0.00123457' in results[1])

if __name__ == '__main__':
    unittest.main()