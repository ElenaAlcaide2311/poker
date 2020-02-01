from deck import Deck
from player import Player
from naipe import Naipe

class Game(object):
    def __init__(self):
        self.deck = Deck()
        self.players = [Player(), Player()]
        self.table = []
    #def __str__(self):
        
        
