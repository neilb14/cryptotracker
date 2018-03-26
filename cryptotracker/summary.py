def build(data):
    results = {}
    for row in data:
        date,exchange,to_currency,from_currency,amount,rate,charge = row
        if(to_currency not in results):
            results[to_currency] = {
                'amount': 0,
                'fees': 0
            }
        if(from_currency not in results):
            results[from_currency] = {
                'amount': 0,
                'fees': 0
            }
        results[to_currency]['amount'] += float(amount)
        results[to_currency]['fees'] += float(charge)
        results[from_currency]['amount'] -= float(amount)*float(rate)
    return results