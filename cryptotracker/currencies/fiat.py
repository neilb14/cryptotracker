class Fiat(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '${:.2f}'.format(self.value)