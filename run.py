import sys
from cryptotracker import cli

if __name__ == '__main__':
    valid_args, message = cli.parse_args(sys.argv[1:])
    if(not valid_args):
        print(message)