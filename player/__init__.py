from naipe import Naipe

class Player(object):
    def __init__(self):
        self.hand = []
        self.table = []
    def __str__(self):
        res = ""
        for n in self.hand:
            res = res + str(n) + " | "
        return res
    def add_naipe(self, n):
        self.hand.append(n)

    def set_table_cards(self, status):
        self.table = status
        
    
    def hand_scoring(self, hand, table):
        self.hand = hand
        self.table = table
        total = self.hand + self.table
        total.sort(key = lambda x: x.number, reverse = False) #Ordena la lista "total" de menor a mayor (numero)
        for i in total:
            print(i)
        par = Player.is_pair(total)
        alta = Player.high_card(total)
        poker = Player.is_poker(total)
        print(poker)

    def high_card(cards):
        return cards[-1]
    def is_pair(cards):
        i = 0
        while i < (len(cards)-2):
            if cards[i].number == cards[i+1].number:
                return [cards[i],cards[i+1]]
            i = i + 1
        return False
    def is_poker(cards):
        i = 0
        while i < (len(cards)-4):
            if cards[i].number == cards[i+3].number:
                return [cards[i], cards[i+1] ,cards[i+2], cards[i+3]]
            i = i + 1
        return False     
    #def is_two_pair
        

            
