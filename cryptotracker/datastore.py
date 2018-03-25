def save(record):
    with open('testfile.csv', 'w') as f:
        f.write(record)