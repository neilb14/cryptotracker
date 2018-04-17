from cryptotracker.currencies.fiat import Fiat

def build(data, price={}):
    results = {}
    for row in data:
        date,exchange,to_currency,from_currency,amount,rate,charge = row
        if(to_currency not in results):
            results[to_currency] = {
                'amount': 0,
                'fees': 0,
                'total_cost': 0,
                'average_price': 0
            }
        if(from_currency not in results):
            results[from_currency] = {
                'amount': 0,
                'fees': 0,
                'total_cost': 0,
                'average_price': 0
            }
        results[to_currency]['amount'] += float(amount)
        results[to_currency]['fees'] += float(charge)
        results[to_currency]['total_cost'] += float(amount)*float(rate)
        results[to_currency]['average_price'] = results[to_currency]['total_cost'] / results[to_currency]['amount']
        results[from_currency]['amount'] -= float(amount)*float(rate)
        if to_currency in price:
            results[to_currency]['price'] = price[to_currency]
            results[to_currency]['value'] = results[to_currency]['amount']*price[to_currency]
    return results