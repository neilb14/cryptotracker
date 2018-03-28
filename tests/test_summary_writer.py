import unittest, io
from datetime import datetime
from cryptotracker import summary_writer

class TestDatastore(unittest.TestCase):
    def test_summary_string_for_single_coin(self):
        summary = {'BTC':{'amount':100,'fees':1}}
        results = summary_writer.write(summary)
        self.assertEqual(1, len(results))
        self.assertEqual('\033[95mBTC\x1b[0m\t\033[92m100\x1b[0m\t\033[94m1\033[0m', results[0])

    def test_summary_string_rounding(self):
        summary = {'BTC':{'amount':100.23456789,'fees':0.00123456789}}
        results = summary_writer.write(summary)
        self.assertEqual('\033[95mBTC\x1b[0m\t\033[92m100.234568\x1b[0m\t\033[94m0.001235\033[0m', results[0])

if __name__ == '__main__':
    unittest.main()