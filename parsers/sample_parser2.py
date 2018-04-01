import re
from datetime import datetime

# 0 date        2017-02-11
# 1 time        18:29:50
# 2 txn type    deposit | buy
# 3 txn method  balance | directdebit
# 4 rate        7636.97,
# 5 cost        20.00,
# 6 amount      1.233548,
# 7 to currency  BTC
# 8 status      completed | expired

def parse(row):
    result = {'valid':True}
    if row[2] != 'buy' or row[8] != 'completed':
        result['valid'] = False
        return result
    date = datetime.strptime(row[0], '%Y-%m-%d')
    result['date'] = date
    result['from_currency'] = 'CAD'
    result['to_currency'] = row[7]
    result['amount'] = float(row[6])
    result['rate'] = float(row[4])
    result['charge'] = 0
    return result