import sys
from cryptotracker import cli, row
from cryptotracker.datastore import Datastore

def main(argv):
    args = cli.parse_args(argv)
    Datastore(args['dir']).save(row.build(args))

if __name__ == '__main__':
    main(sys.argv[1:])