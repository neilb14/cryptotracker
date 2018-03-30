class Crypto(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{:.6f}'.format(self.value)