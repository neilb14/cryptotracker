def build(args):
    result = []
    result.append(args['date'].strftime('%m/%d/%Y'))
    result.append(args['exchange'])
    result.append(args['to_currency'])
    result.append(args['from_currency'])
    result.append(args['amount'])
    result.append(args['rate'])
    result.append(args['charge'])
    return result