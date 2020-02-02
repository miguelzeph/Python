""" Jogo de Cartas """

import random

class Card(object):

    def __init__(self, suit, val):

        self.suit = suit #Naipe
        self.value = val #Valor

    def show(self):

        print(f'{self.value} of {self.suit} ')


class Deck(object):

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):

        for s in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:

            for v in range(1,14):

                if v == 1:
                    v = "A"
                if v == 11:
                    v = "Queen"
                if v == 12:
                    v = "Jack"
                if v == 13:
                    v = "King"


                self.cards.append(Card(s,v))



    def show(self):

        for c in self.cards:

            c.show()

    def shuffle(self):

        for i in range(len(self.cards)-1,0,-1):

            r = random.randint(0,i)

            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):

        return self.cards.pop()

class Player(object):

    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):

        self.hand.append(deck.draw_card())

        return self #Assim posso comprar varias cartas

    def show_hand(self):

        for card in self.hand:

            card.show()

    def discard(self):

        self.hand.pop()

        return self




#card = Card('Clubs',6)

#card.show()

deck = Deck()
#deck.show() #Antes de Embaralhar
deck.shuffle() #Embaralhar
#deck.show() #Depois de Embaralhar

bob = Player("Bob")
bob.draw(deck).draw(deck).draw(deck)
bob.show_hand()
print('\n')
bob.discard().discard() #Discartei 2 cartas
bob.show_hand()

#card = deck.draw_card()
#card.show()

