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
            
            if cards[i].suit != 3:
                return False

            if cards[i].number < 10 and cards[i].number != 1:
                return False
            i = i+1
        return True

    @staticmethod
    def straight_flush(cards): #escalera de color y palo
        color = -1
        suit = -1
        scoring = -1
        i = 0
        while i < (len(cards)):
            if color == -1:
                color = cards[i].color
            elif cards[i].color != color:
                return False

            if suit == -1:
                suit = cards[i].suit
            elif cards[i].suit != suit:
                return False
            
            if scoring == -1:
                scoring = cards[i].number
            elif scoring != (cards[i].number - i):
                return False
            
            i = i+1
        return True

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
        pair_1 = Player.pair(cards)
        pair_2 = Player.pair(cards[::-1])
        three_of_a_kind = Player.three_of_a_kind(cards)
        if pair_1 and pair_2 and three_of_a_kind:
            if pair_1[0].number != three_of_a_kind[0].number:
                return pair_1 + three_of_a_kind
            elif pair_2[0].number != three_of_a_kind[0].number:
                return pair_2 + three_of_a_kind
            else:
                return False
        return False

    #color
    @staticmethod
    def flush(cards): #cartas del mismo color y palo
        i = 1
        color = cards[0].color
        suit = cards[0].suit
        while i < len(cards):
            if cards[i].color != color or cards[i].suit != suit:
                return False
            i = i+1
        return True

    #Straight
    @staticmethod
    def straight(cards): #escalera
        i = 0
        while i < (len(cards)-1):
            if cards[i].number != cards[i+1].number -1:
                if cards[i].number == 1 and cards[i+1].number == 10:
                    i = i+1
                    continue
                else:
                    return False
            i = i+1
        return True

    #Three of a kind
    @staticmethod
    def three_of_a_kind(cards): #3 cartas del mismo valor
        i = 0
        while i < (len(cards)-3):
            if cards[i].number == cards[i+1].number and cards[i].number == cards[i+2].number:
                return [cards[i],cards[i+1], cards[i+2]]
            i = i + 1
        return False

    #Two Pair
    @staticmethod
    def double_pair(cards): #2 parejas
        pair_1 = Player.pair(cards)
        pair_2 = Player.pair(cards[::-1])#reverse array
        if pair_1 and pair_2:
            if pair_1[0].number != pair_2[0].number:
                return pair_1 + pair_2
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
        

            
