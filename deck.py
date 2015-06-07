"""
This module contains the Deck and Card classes that
control the logic of the game
"""
class Deck():
    """
    Represents a deck of playing cards
    """
    suit_names = ["clubs", "diamonds", "hearts", "spades"]
    rank_names = ["ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "jack", "queen", "king"]
    cards = []
    def __init__(self):
        #Create all the cards
        for s in self.suit_names:
            for r in self.rank_names:
                temp_card = Card(s,r)
                self.cards.append(temp_card)
    
    def shuffle(self):
        pass
    
    
class Card():
    """
    Represents a single card
    """
    suit = 0
    rank= 0
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return (self.rank + " of " + self.suit)
    
    def value(self):
        if(self.rank == 'ace'):
            return 11
        elif(self.rank in ["jack", "queen", "king"]):
            return 10
        else:
            return int(self.rank)
            