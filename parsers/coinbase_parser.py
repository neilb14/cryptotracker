import pprint,re
from datetime import datetime

# 0 Timestamp                   2016-09-28 11:51:48 -0700
# 1 Balance                     4.56987317
# 2 Amount                      0.25980213
# 3 Currency                    BTC
# 4 To                          57a837eac60dbb1239e6aca8
# 5 Notes                       Bought 0.05988317 BTC for $50.00 CAD.,
# 6 Instantly Exchanged         false,
# 7 Transfer Total              50.0,
# 8 Transfer Total Currency     CAD,
# 9 Transfer Fee                1.92,
# 10 Transfer Fee Currency      CAD,
# 11 Transfer Payment Method    Visa credit ********1234,
# 12 Transfer ID                57a4965a0eaf29c100eeea82,
# 13 Order Price                "",
# 14 Order Currency             "",
# 15 Order BTC                  "",
# 16 Order Tracking Code        "",
# 17 Order Custom Parameter     "",
# 18 Order Paid Out             "",
# 19 Recurring Payment ID       ""
# 20 Coinbase ID (visit https://www.coinbase.com/transactions/[ID] in your browser),Bitcoin Hash (visit https://www.coinbase.com/tx/[HASH] in your browser for more info)

def parse(row):
    result = {'valid':True}
    date = datetime.strptime(row[0].split()[0], '%Y-%m-%d')
    result['date'] = date
    result['from_currency'] = row[8]
    result['to_currency'] = row[3]
    result['amount'] = float(row[2])
    if row[7] == '':
        result['valid'] = False
        return result
    rate = float(row[7])/float(row[2])
    result['rate'] = rate
    result['charge'] = float(row[9])/rate
    return result