import json, urllib

class PriceService():
    def get_price(self, coin):
        contents = urllib.request.urlopen("https://min-api.cryptocompare.com/data/price?fsym={}&tsyms=CAD".format(coin)).read()
        data = json.loads(contents.decode("utf-8"))
        return float(data['CAD'])