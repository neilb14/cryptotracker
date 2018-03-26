import unittest, io
from datetime import datetime
from cryptotracker import summary_writer

class TestDatastore(unittest.TestCase):
    def test_summary_string_for_single_coin(self):
        summary = {'BTC':{'amount':100,'fees':1}}
        results = summary_writer.write(summary)
        self.assertEqual(1, len(results))
        self.assertEqual('BTC\r\n  Amount: 100\r\n  Fees: 1\r\n', results[0])

    def test_summary_string_rounding(self):
        summary = {'BTC':{'amount':100.23456789,'fees':0.00123456789}}
        results = summary_writer.write(summary)
        self.assertEqual('BTC\r\n  Amount: 100.234568\r\n  Fees: 0.001235\r\n', results[0])

if __name__ == '__main__':
    unittest.main()