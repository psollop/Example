import random

class Card:
    def __init__(self, suit:str, value:str):
        self.suit = suit
        self.value = value
        
    def __str__(self):
        return f"{self.value} of {self.suit}"

class Hand:
    def __init__(self):
        self.cards = []
        
    def draw(self, deck):
        self.cards.append(deck.deal())
        
    def discard(self, card):
        self.cards.remove(card)
        
    def receive(self, cards):
        self.cards.extend(cards)
        
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

class Deck:
    def __init__(self, suits:list, values:list):
        self.cards = [Card(suit, value) for suit in suits for value in values]
        
    def deal(self):
        return self.cards.pop(0)
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def __str__(self):
        return f"Deck of {len(self.cards)} cards"
    
class SpanishDeck(Deck):
    def __init__(self):
        suits = ["Oros", "Copas", "Espadas", "Bastos"]
        values = ["As", "2", "3", "4", "5", "6", "7", "Sota", "Caballo", "Rey"]
        super().__init__(suits, values)
        
class EnglishDeck(Deck):
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        super().__init__(suits, values)

if __name__ == "__main__":
    # Test Card
    card = Card("Hearts", "Ace")
    print(card)
    
    # Test Hand
    hand = Hand()
    deck = Deck(["Hearts", "Diamonds", "Clubs", "Spades"], ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"])
    hand.draw(deck)
    hand.draw(deck)
    print(hand)
    hand.discard(hand.cards[0])
    print(hand)
    hand.receive([deck.deal(), deck.deal()])
    print(hand)
    
    # Test Deck
    deck = Deck(["Hearts", "Diamonds", "Clubs", "Spades"], ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"])
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())
    print(deck)
    
    # Test SpanishDeck
    spanish_deck = SpanishDeck()
    print(spanish_deck)
    spanish_deck.shuffle()
    print(spanish_deck)
    print(spanish_deck.deal())
    print(spanish_deck)
    
    # Test EnglishDeck
    english_deck = EnglishDeck()
    print(english_deck)
    english_deck.shuffle()
    print(english_deck)
    print(english_deck.deal())
    print(english_deck)
