from deck import Deck
from player import Player
from naipe import Naipe

class Game(object):
    def __init__(self):
        self.deck = Deck()
        self.players = [Player(), Player()]
        self.table = []
    def __str__(self):
        res = ""
        for n in self.players:
            res = res + str(n) + "\n"

        for m in self.table:
            res = res + str(m) + " | "
        return res
    def start(self):
        self.deck.shuffle()
        for i in range(2):
            for j in self.players:
                j.add_naipe(self.deck.pop())
        for i in range(3):
            self.table.append(self.deck.pop())
        

    
        
