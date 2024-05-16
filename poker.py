import random
class Card:
    SUITS = ["♠", "♥", "♣", "♦"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "Q", "K", "A"]

    def __init__(self, rank, suit):             #this method is a magic method, magic method gets called by itself when something happens
        if rank not in self.RANKS:
            raise Exception(f"Invalid rank, must be one of {self.RANKS}")
        if suit not in self.SUITS:
            raise Exception(f"Invalid suit, must be one of {self.SUITS}")
        self._rank = rank
        self._suit = suit

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        cards = []
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                card = Card(rank, suit)
                cards.append(card)
        self._cards = tuple(cards)

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

    def shuffle(self):
        # shuffles the cards in the deck
        # taking the list of cards and mixing in a random order
        cards = list(self.cards)
        random.shuffle(cards)
        self._cards = tuple(cards)

class Hand:
    def __init__(self, deck):
        # deck is shuffled before
        cards =[]
        for i in range(5):
            cards.append(deck.cards[i])
        self._cards = tuple(cards)

    def __str__(self):
        return str(self._cards)

    @property
    def cards(self):
        return self._cards

    @property                   # tell us if a random collection of cards in the deck is a flush
    def is_flush(self):
        suit = self._cards[0].suit
        for i in range(1,5):
            if self._cards[i].suit != suit:
                return False

        return True

    @property
    def is_pair(self):
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        for rank in ranks:
            if ranks.count(rank) == 2:
                return True
            return False

    @property
    def is_3_kind(self):
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        for rank in ranks:
            if ranks.count(rank) == 3:
                return True
            return False

    @property
    def is_4_kind(self):
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        for rank in ranks:
            if ranks.count(rank) == 4:
                return True
            return False

    @property
    def is_full_house(self):
        return self.is_3_kind and self.is_pair

    @property
    def is_2_pair(self):
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        ranks = set(ranks)
        if len(ranks) == 3 and not self.is_3_kind


# precision = tries = 10
# i = 0
# while True:
#    i = i + 1
#    d = Deck()
#    d.shuffle()
#    hand = Hand(d)
#    if hand.is_flush:
#        tries -= 1

#    if tries == 0:
#        break

# probability = precision/i * 100
# print(f"the odds of getting a flush are {probability}%")

# precision = tries = 1000
# i = 0
# while True:
#    i = i + 1
#    d = Deck()
#    d.shuffle()
#    hand = Hand(d)
#    if hand.is_pair:
#        tries -= 1

#    if tries == 0:
#        break

# probability = precision/i * 100
# print(f"the odds of getting a pair are {probability}%")

# precision = tries = 1000
# i = 0
# while True:
#    i = i + 1
#    d = Deck()
#    d.shuffle()
#    hand = Hand(d)
#    if hand.is_full_house:
#        tries -= 1

#    if tries == 0:
#        break

# probability = precision/i * 100
# print(f"the odds of getting a full house are {probability}%")

precision = tries = 100
i = 0
while True:
    i = i + 1
    d = Deck()
    d.shuffle()
    hand = Hand(d)
    if hand.is_2_pair:
        tries -= 1

    if tries == 0:
        break

probability = precision/i * 100
print(f"the odds of getting a full house are {probability}%")











