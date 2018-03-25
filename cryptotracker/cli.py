import argparse

parser = argparse.ArgumentParser(description='CryptoTracker - keep track of your crypto trades')

parser.add_argument('--from', dest='from_currency', default='CAD', help='transfer from currency')
parser.add_argument('--to', dest='to_currency', default='BTC', help='transfer to currency')
parser.add_argument('--amount', required=True, help='purchsed quantity')
parser.add_argument('--rate', required=True, help='exchange rate')
parser.add_argument('--charge', default=0, help='charge for transfer')
parser.add_argument('--dir', default='data', help='directory containing csv files. If folder doesnt already exist it will be created.')

def parse_args(args):
    return vars(parser.parse_args(args))