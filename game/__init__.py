from deck import Deck
from player import Player
from naipe import Naipe

class Game(object):
    def __init__(self, players, minor, major):
        self.deck = Deck()
        self.players = players
        self.table = []
        self.bets = []
        for i in self.players:
            self.bets.append(-1)
        self.round = 0
        self.minor = minor
        self.major = major
    
    def __str__(self):
        res = ""

        res = res + "Round "+str(self.round)+"\nMinor "+str(self.minor)+ "$ Major "+str(self.major)+"$\n"

        res = res+"\nPlayers: \n"
        for n in self.players:
            res = res + "\t" + str(n) + "\n"

        res = res + "\nTable:\n"
        for m in self.table:
            res = res + str(m) + " | "

        res = res + "\nBets:\n"
        for b in self.bets:
            res = res + str(b)+ " | "
        return res
    
    def start(self):
        self.bets[-1] = self.players[-1].bet(self.minor/2)
        self.bets[-2] = self.players[-2].bet(self.minor)

        self.deck.shuffle()
        for i in range(2):
            for j in self.players:
                j.add_naipe(self.deck.pop())
        #for i in range(5):
        #    self.table.append(self.deck.pop())
        
    
    
        
