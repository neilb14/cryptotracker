import sys, argparse
import urllib.request
from cryptotracker import row, summary, summary_writer
from cryptotracker.datastore import Datastore
from cryptotracker.price_service import PriceService


def main(args):
    parser = argparse.ArgumentParser(description='Summary - prints a summary of your portfolio')
    parser.add_argument('-x', '--dir', default='./data', help='directory containing csv data files. If folder doesnt already exist it will be created.')
    parser.add_argument('-v', '--value', help='include current value of portfolio.', action='store_true')
    config = parser.parse_args(args)
    price = {}
    if config.value:
        price['BTC'] = PriceService().get_price('BTC')
        price['BCH'] = PriceService().get_price('BCH')
        price['ETH'] = PriceService().get_price('ETH')
        price['LTC'] = PriceService().get_price('LTC')

    ds = Datastore(config.dir)
    for coin_summary in summary_writer.write(summary.build(ds.read_all(), price), price):
        print(coin_summary)

if __name__ == '__main__':
    main(sys.argv[1:])