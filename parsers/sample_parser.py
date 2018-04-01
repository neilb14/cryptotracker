import pprint,re
from datetime import datetime

def parse(row):
    result = {}
    date = datetime.strptime(row[0], '%d-%m-%y')
    result['date'] = date
    result['from_currency'] = row[1]
    result['to_currency'] = row[3]
    result['amount'] = float(row[4])
    rate = re.sub('[",]', '', row[5])
    result['rate'] = float(rate)
    result['charge'] = 0
    return result