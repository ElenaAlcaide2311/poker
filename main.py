from naipe import Naipe
from deck import Deck
from player import Player
from game import Game


#g = Game()
#g.start()
#print(g)
h = [Naipe(1,1,1), Naipe(1,0,1)]
t = [Naipe(1,0,3), Naipe(2,1,2), Naipe(7,1,1)]
p = Player()
p.hand_scoring(h,t)
