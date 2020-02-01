from deck import Deck
from player import Player

pl = Player()
a = Deck()
a.shuffle()
print(a)
p = a.pop()
pl.add_naipe(p)
print(pl)


