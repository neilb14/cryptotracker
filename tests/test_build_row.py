import unittest, io
from cryptotracker import row

class TestBuildRow(unittest.TestCase):
    def test_order_of_columns(self):
        args = {
            'date': '2018-03-25',
            'exchange': 'Coinbase',
            'from_currency': 'CAD',
            'to_currency': 'BTC',
            'amount': '1',
            'rate': '11111',
            'fee': '0.0005',
        }
        result = row.build(args)
        self.assertEqual(7, len(result))
        self.assertEqual(args['date'], result[0])
        self.assertEqual(args['exchange'], result[1])
        self.assertEqual(args['to_currency'], result[2])
        self.assertEqual(args['from_currency'], result[3])
        self.assertEqual(args['amount'], result[4])
        self.assertEqual(args['rate'], result[5])
        self.assertEqual(args['fee'], result[6])


if __name__ == '__main__':
    unittest.main()