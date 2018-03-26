import csv

class Datastore():
    def __init__(self, folder):
        self.folder_name = folder
        self.file_name = 'transactions.csv'

    def filename(self):
        return '{}/{}'.format(self.folder_name, self.file_name)
    
    def save(self, record):
        with open(self.filename(), 'a+') as f:
            writer = csv.writer(f)
            writer.writerow(record)

    def read_all(self):
        results = []
        with open(self.filename(), 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                results.append(row)
        return results