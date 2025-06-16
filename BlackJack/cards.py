from random import randrange

from constants import DISPLAY_RANKS, DISPLAY_SUITS, RANKS, SUITS


class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} {DISPLAY_RANKS[self.rank]} - {self.suit} {DISPLAY_SUITS[self.suit]}"


class Deck:
    def __init__(self):
        self.create_deck()

    def create_deck(self):
        cards: list[Card] = []

        for rank in RANKS:
            for suit in SUITS:
                cards.append(Card(rank, suit))

        self.cards = cards

    def get_random_card(self):
        index = randrange(len(self.cards))

        card = self.cards[index]

        del self.cards[index]

        if not len(self.cards):
            self.create_deck()

        return card

    def __str__(self):
        display_cards = []

        for card in self.cards:
            display_rank = DISPLAY_RANKS[card.rank]
            display_suit = DISPLAY_SUITS[card.suit]
            display_cards.append(f"|{display_rank}{display_suit} |")

        return "---".join(display_cards)


__all__ = ["suits", "ranks", "values", "DISPLAY_RANKS", "DISPLAY_SUITS"]
