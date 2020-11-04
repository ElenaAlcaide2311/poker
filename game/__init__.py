from deck import Deck
from player import Player
from naipe import Naipe

class Game(object):
    def __init__(self, number_players, minor, major):
        self.deck = Deck()
        self.players = []
        for i in range(number_players):
            self.players.append(Player("Player "+str(i)))
        self.table = []
        self.round = 0
        self.minor = minor
        self.major = major
    
    def __str__(self):
        res = ""

        res = res + "Round "+str(self.round)+" Minor "+str(self.minor)+ " Major "+str(self.major)+"\n"

        res = res+"\nPlayers: \n"
        for n in self.players:
            res = res + "\t" + str(n) + "\n"

        res = res + "\nTable:\n"
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
        

    
        
