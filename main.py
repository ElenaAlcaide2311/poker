from naipe import Naipe
from deck import Deck
from player import Player
from game import Game


#g = Game()
#g.start()
#print(g)

#number, color, suit

h = [Naipe(10,1,2), Naipe(11,1,3)]
t = [Naipe(1,1,3), Naipe(12,1,3), Naipe(13,1,3)]
p = Player()
scoring=p.hand_scoring(h,t)

print(scoring)



