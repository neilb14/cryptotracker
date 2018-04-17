from cryptotracker.currencies import currency_factory
from cryptotracker.currencies.fiat import Fiat

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def write_color(text, color, bold=False):
    return (colors.BOLD if bold else '') + color + text + colors.ENDC

def tab(column):
    return '{:20}'.format(str(column))

def write(summary, price={}):
    currency_header = '{:6}'.format('Coin')
    amount_header = tab('Amount')
    fees_header = tab('Fees')
    average_price = tab('Average')
    current_price = tab('Price')
    value = tab('Value')
    header = ' '.join([write_color(currency_header, colors.HEADER, True),
                    write_color(amount_header, colors.HEADER, True),
                    write_color(fees_header, colors.HEADER, True), 
                    write_color(average_price, colors.HEADER, True)])
    if len(price) > 0:
        header += ' '.join([write_color(current_price, colors.HEADER, True), write_color(value, colors.HEADER, True)])
    results = [header]
    for currency in sorted(summary.keys()):
        amount = tab(currency_factory.create(currency, float(summary[currency]['amount'])))
        fees = tab(round(summary[currency]['fees'], 8))
        average_price = tab(Fiat(summary[currency]['average_price']))
        row = ' '.join([
            write_color('{:6}'.format(currency), colors.OKBLUE, True), 
            write_color(amount, colors.OKGREEN), 
            write_color(fees, colors.OKBLUE), 
            write_color(average_price, colors.OKGREEN)])
        if currency in price:
            current_price = tab(Fiat(price[currency]))
            row += ' ' + write_color(current_price, colors.OKGREEN)
        if 'value' in summary[currency]:
            value = tab(Fiat(summary[currency]['value']))
            row += ' ' + write_color(value, colors.OKBLUE)
        results.append(row)        
    return results