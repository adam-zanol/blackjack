class Deck():
    """
    Represents a deck of playing cards
    """
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = ["Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]
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