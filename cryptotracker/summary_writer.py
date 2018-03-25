def write(summary):
    results = []
    for currency in summary:
        results.append('{}:\r\n  Amount: {}\r\n  Fees: {}\r\n'.format(currency, summary[currency]['amount'], summary[currency]['fees']))
    return results