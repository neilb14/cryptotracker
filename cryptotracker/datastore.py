class Datastore():
    def __init__(self, folder):
        self.folder_name = folder
        self.file_name = 'transactions.csv'

    def save(self, record):
        with open('{}/{}'.format(self.folder_name, self.file_name), 'w') as f:
            f.write(record)