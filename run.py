import sys
from cryptotracker import cli, row, summary, summary_writer
from cryptotracker.datastore import Datastore

def main(argv):
    args = cli.parse_args(argv)
    ds = Datastore(args['dir'])
    if(args['info']):
        for coin_summary in summary_writer.write(summary.build(ds.read_all())):
            print(coin_summary)
    elif('amount' in args and args['amount'] is not None and 'rate' in args and args['rate'] is not None):
        ds.save(row.build(args))
    else:
        cli.print_help()

if __name__ == '__main__':
    main(sys.argv[1:])