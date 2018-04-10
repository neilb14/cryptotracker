import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description='CryptoTracker - keep track of your crypto trades')
parser.add_argument('-d', '--date', help='date of transaction (default is today)')
parser.add_argument('-e', '--exchange', default='Coinbase', help='exchange that processed the transaction')
parser.add_argument('-f', '--from', dest='from_currency', default='CAD', help='transfer from currency')
parser.add_argument('-t', '--to', dest='to_currency', default='BTC', help='transfer to currency')
parser.add_argument('-a', '--amount', help='purchsed quantity')
parser.add_argument('-r', '--rate', help='exchange rate')
parser.add_argument('-c', '--charge', default=0, help='charge for transfer')
parser.add_argument('-x', '--dir', default='./data', help='directory containing csv data files. If folder doesnt already exist it will be created.')

def parse_args(args):
    result = vars(parser.parse_args(args))
    if('date' not in result or result['date'] is None):
        result['date'] = datetime.now()
    else:
        result['date'] = datetime.strptime(result['date'],'%m/%d/%Y')
    return result

def print_help():
    print(parser.print_help())
