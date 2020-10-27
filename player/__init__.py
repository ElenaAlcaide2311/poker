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

        if Player.royal_straight_flush(total):
            return [10, total]

        if Player.straight_flush(total):
            return [9, total]
        
        poker = Player.poker(total)
        if poker:
            return [8,[poker]]

        full_house = Player.full_house(total)
        if full_house:
            return [7,full_house]

        if Player.flush(total):
            return [6,total]
        
        if Player.straight(total):
            return [5,total]

        three_of_a_kind = Player.three_of_a_kind(total)
        if three_of_a_kind:
            return [4,three_of_a_kind]

        double_pair = Player.double_pair(total)
        if double_pair:
            return [3,double_pair]
        
        pair = Player.pair(total)
        if pair:
            return [2,pair]

        return [1, Player.high_card(total)]

    @staticmethod
    def royal_straight_flush(cards): #escalera real 10, J, Q, K, A de ♣
        color = -1
        i = 0
        while i < (len(cards)):
            if color == -1:
                color = cards[i].color
            elif cards[i].color != color:
                return False
            elif cards[i].suit != 3:
                return False
            elif cards[i].number < 10 & cards[i].number != 1:
                return False
            i = i+1
        return True

    @staticmethod
    def straight_flush(cards): #escalera de color
        color = -1
        i = 0
        return False
        #while i < (len(cards)):

    #Poker 4 cartas iguales valor
    @staticmethod
    def poker(cards): 
        i = 0
        while i < (len(cards)-4):
            if cards[i].number == cards[i+3].number:
                return [cards[i], cards[i+1] ,cards[i+2], cards[i+3]]
            i = i + 1
        return False 

    #Full House (3 cartas del mismo y otras 2 de otro)
    @staticmethod
    def full_house(cards):
        return False

    #color
    @staticmethod
    def flush(cards): #cartas del mismo color y palo
        return False

    #Straight
    @staticmethod
    def straight(cards): #escalera
        return False

    #Three of a kind
    @staticmethod
    def three_of_a_kind(cards): #3 cartas del mismo valor
        return False

    #Two Pair
    @staticmethod
    def double_pair(cards): #2 parejas
        return False

    #Pair
    @staticmethod
    def pair(cards):
        i = 0
        while i < (len(cards)-2):
            if cards[i].number == cards[i+1].number:
                return [cards[i],cards[i+1]]
            i = i + 1
        return False

    #High Card
    @staticmethod
    def high_card(cards):
        return cards[-1]
        

            
