class Naipe(object):
    def __init__(self, number, color, suit):
        self.number = number
        self.color = color
        self.suit = suit

    def __str__(self):
        res = " "
        if self.number < 11:
            res = res + str(self.number)
        elif self.number == 11:
            res = res + "J"
        elif self.number == 12:
            res = res + "Q"
        else:
            res = res + "K"

        if self.color == 0:
            if self.suit == 0:
                res = res + "♢"
            elif self.suit == 1:
                res = res + "♡"
            elif self.suit == 2:
                res = res + "♤"
            else:
                res = res + "♧"
        else:
            if self.suit == 0:
                res = res + "♦"
            elif self.suit == 1:
                res = res + "♥"
            elif self.suit == 2:
                res = res + "♠"
            else:
                res = res + "♣"

        return res

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
    

a = Deck()
print(a)
