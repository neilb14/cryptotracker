import unittest, io
from datetime import datetime
from cryptotracker import summary

class TestDatastore(unittest.TestCase):
    def setUp(self):
        self.timestamp = datetime.now().strftime('%m/%d/%Y')
        self.data = [[self.timestamp,'abc','BTC','CAD',0.1,1197,0.0025],
                [self.timestamp,'abc','BTC','CAD',0.25,1165,0.0025],
                [self.timestamp,'abc','BTC','CAD',0.3,1125,0.005],
                [self.timestamp,'abc','ETH','CAD',1,660,0.001],
                [self.timestamp,'abc','ETH','CAD',1,700,0.001]]

    def test_summary_calculates_a_single_coin(self):
        result = summary.build(self.data[:3])
        self.assertAlmostEqual(0.65, result['BTC']['amount'])
        self.assertEqual(0.01, result['BTC']['fees'])
        self.assertAlmostEqual((0.1*1197+0.25*1165+0.3*1125)*-1, result['CAD']['amount'])

    def test_summary_calculates_multiple_coins(self):
        result = summary.build(self.data)
        self.assertAlmostEqual(0.65, result['BTC']['amount'])
        self.assertEqual(0.01, result['BTC']['fees'])
        self.assertEqual(2, result['ETH']['amount'])
        self.assertEqual(0.002, result['ETH']['fees'])
        self.assertAlmostEqual((0.1*1197+0.25*1165+0.3*1125)*-1-660-700, result['CAD']['amount'])

if __name__ == '__main__':
    unittest.main()