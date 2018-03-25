import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description='CryptoTracker - keep track of your crypto trades')

parser.add_argument('--date', help='date of transaction (default is today)')
parser.add_argument('--exchange', default='Coinbase', help='exchange that processed the transaction')
parser.add_argument('--from', dest='from_currency', default='CAD', help='transfer from currency')
parser.add_argument('--to', dest='to_currency', default='BTC', help='transfer to currency')
parser.add_argument('--amount', required=True, help='purchsed quantity')
parser.add_argument('--rate', required=True, help='exchange rate')
parser.add_argument('--charge', default=0, help='charge for transfer')
parser.add_argument('--dir', default='./data', help='directory containing csv files. If folder doesnt already exist it will be created.')

def parse_args(args):
    result = vars(parser.parse_args(args))
    if('date' not in result or result['date'] is None):
        result['date'] = datetime.now()
    return result