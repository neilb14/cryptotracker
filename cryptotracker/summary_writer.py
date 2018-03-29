
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

def write(summary):
    currency_header = '{:6}'.format('Coin')
    amount_header = '{:>20}'.format('Amount')
    fees_header = '{:>20}'.format('Fees')
    results = [
        ' '.join([write_color(currency_header, colors.HEADER, True),write_color(amount_header, colors.HEADER, True),write_color(fees_header, colors.HEADER, True)])
    ]
    for currency in sorted(summary.keys()):
        amount = '{:20}'.format(round(summary[currency]['amount'], 6))
        fees = '{:20}'.format(round(summary[currency]['fees'], 8))
        results.append(' '.join([write_color('{:6}'.format(currency), colors.HEADER), write_color(amount, colors.OKGREEN), write_color(fees, colors.OKBLUE)]))        
    return results