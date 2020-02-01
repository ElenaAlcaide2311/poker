from naipe import Naipe

class Player(object):
    def __init__(self):
        self.hand = []
    def __str__(self):
        res = ""
        for n in self.hand:
            res = res + str(n) + " | "
        return res
    def add_naipe(self, n):
        self.hand.append(n)
