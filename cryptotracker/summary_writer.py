

def write(summary):
    results = []
    for currency in summary:
        results.append('{}\r\n  Amount: {}\r\n  Fees: {}\r\n'.format(currency, round(summary[currency]['amount'], 6), round(summary[currency]['fees'], 6)))
    return results