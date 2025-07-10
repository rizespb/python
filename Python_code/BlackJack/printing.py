from cards import DISPLAY_RANKS, DISPLAY_SUITS, Card, Deck
from constants import DISPLAY_RANKS, DISPLAY_SUITS


def print_card(card: Card):
    rank = DISPLAY_RANKS[card.rank]
    suit = DISPLAY_SUITS[card.suit]

    print(
        f""" ___
|{rank}{"" if rank =='10' else ' '} |
|   |
| {suit} |
 ‾‾‾"""
    )


def print_cards(cards: list[Card]):
    length = len(cards)

    top = " ".join([" ___ "] * length)
    bottom = " ".join([" ‾‾‾ "] * length)

    ranks = map(lambda card: DISPLAY_RANKS[card.rank], cards)
    ranks_display = " ".join(
        [f"|{rank}{"" if rank =='10' else ' '} |" for rank in ranks]
    )

    middle = " ".join(["|   |"] * length)

    suits = map(lambda card: DISPLAY_SUITS[card.suit], cards)
    suits_display = " ".join([f"| {suit} |" for suit in suits])

    print(
        f"""{top}
{ranks_display}
{middle}
{suits_display}
{bottom}"""
    )
