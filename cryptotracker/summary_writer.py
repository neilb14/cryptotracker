
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
    results = []
    for currency in sorted(summary.keys()):
        amount = str(round(summary[currency]['amount'], 6))
        fees = str(round(summary[currency]['fees'], 6))
        results.append('\t'.join([write_color(currency, colors.HEADER), write_color(amount, colors.OKGREEN), write_color(fees, colors.OKBLUE)]))        
    return results