from naipe import Naipe
import random

class Deck(object):
    def __init__(self):
        self.naipes = []
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        colors = [0, 1]     #red = 0, black = 1
        suits = [0, 1, 2 ,3]    #0 = diamonds, 1 = hearts, 2 = spades, 3 = clubs
        for s in suits:
            for c in colors:
                for n in numbers:
                    self.naipes.append(Naipe(n,c,s))

    def __str__(self):
        res = ""
        for n in self.naipes:
            res = res + str(n) + " | "
        return res

    def shuffle(self):
        random.shuffle(self.naipes)
 

