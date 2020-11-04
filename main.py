from naipe import Naipe
from deck import Deck
from player import Player
from game import Game


g = Game(2,1,2)
g.start()
print(g)

print("\n")
print ("Scoring")

for p in g.players:
    score = p.hand_scoring(g.table)
    print("\t"+p.name)
    print(score)

#number, color, suit

#h = [Naipe(1,1,2), Naipe(11,1,3)]
#t = [Naipe(1,1,3), Naipe(11,1,3), Naipe(1,1,3)]
#p = Player()
#scoring=p.hand_scoring(h,t)
#
#print(scoring)



