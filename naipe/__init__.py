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
