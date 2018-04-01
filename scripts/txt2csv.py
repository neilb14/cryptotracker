import sys, csv, os

def main(args):
    txt_filename = args[0]
    base_filename = os.path.splitext(txt_filename)[0]
    csv_filename = base_filename + '.csv'
    print('Converting {} to {}'.format(txt_filename, csv_filename))
    with open(txt_filename, 'r') as txt_file:
        with open(csv_filename, 'w') as csv_file:
            writer = csv.writer(csv_file)
            for line in txt_file.readlines():
                writer.writerow(line.split())

if __name__ == '__main__':
    main(sys.argv[1:])