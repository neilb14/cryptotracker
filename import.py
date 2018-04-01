import sys, importlib, csv, argparse
from cryptotracker import row
from cryptotracker.datastore import Datastore

def main(args):
    parser = argparse.ArgumentParser(description='Importer - bulk import from an exchange transaction export csv file')
    parser.add_argument('-x', '--dir', default='./data', help='directory containing csv data files. If folder doesnt already exist it will be created.')
    parser.add_argument('-p', '--parser', required=True, help='parser module to use.')
    parser.add_argument('-f', '--file', required=True, help='specify the file to import.')
    parser.add_argument('-e', '--exchange', required=True, help='exchange in which transactions took place.')
    parser.add_argument('--dry-run', help='extract transactions but do not save in db', action='store_true')
    config = parser.parse_args(args)

    print('Importing {}'.format(config.file))
    print('Using {}'.format(config.parser))
    parser = importlib.import_module(config.parser)

    transactions = []
    with open(config.file, 'r') as f:
        reader = csv.reader(f)
        for record in reader:
            transactions.append(parser.parse(record))

    ds = Datastore(config.dir)
    for t in transactions:
        if not t['valid']:
            continue
        print('{0:6}{1:20}{2:30}{3:30}'.format(t['to_currency'], t['amount'], t['rate'], t['charge']))
        t['exchange'] = config.exchange
        if config.dry_run:
            continue
        ds.save(row.build(t))

    print(len(transactions))

if __name__ == '__main__':
    main(sys.argv[1:])