import sys
from cryptotracker import cli, row
from cryptotracker.datastore import Datastore

def main(argv):
    args = cli.parse_args(argv)
    ds = Datastore(args['dir'])
    if('amount' in args and args['amount'] is not None and 'rate' in args and args['rate'] is not None):
        ds.save(row.build(args))
    else:
        cli.print_help()

if __name__ == '__main__':
    main(sys.argv[1:])