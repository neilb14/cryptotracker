import sys, argparse
from cryptotracker import row, summary, summary_writer
from cryptotracker.datastore import Datastore

def main(args):
    parser = argparse.ArgumentParser(description='Summary - prints a summary of your portfolio')
    parser.add_argument('-x', '--dir', default='./data', help='directory containing csv data files. If folder doesnt already exist it will be created.')
    parser.add_argument('-p', '--price', help='include current price.', action='store_true')
    config = parser.parse_args(args)

    ds = Datastore(config.dir)
    for coin_summary in summary_writer.write(summary.build(ds.read_all())):
        print(coin_summary)

if __name__ == '__main__':
    main(sys.argv[1:])