from cards import Card, Deck
from constants import TARGET, VALUES
from printing import print_cards


class Player:
    def __init__(self, name: str):
        self.name = name

    def init_hand(self, deck: Deck):
        self.hand = Hand()

        self.hand.add_card(deck.get_random_card())
        self.hand.add_card(deck.get_random_card())


class User(Player):
    def __init__(self, name: str):
        super().__init__(name)

        self.balance = 100
        self.hand = Hand()

    def lost_bet(self, amount: int) -> None:
        self.balance -= amount

        print(
            f"Игрок {self.name} проиграл \033[31m{amount}$\033[0m. Текущий баланс \033[36m{self.balance}$\033[0m\n"
        )

    def win_bet(self, amount: int) -> None:
        self.balance += amount

        print(
            f"Игрок {self.name} выграл \033[36m{amount}$\033[0m. Текущий баланс \033[36m{self.balance}$\033[0m\n"
        )

    @property
    def is_loser(self) -> bool:
        return self.balance <= 0


class Dealer(Player):
    def __init__(self):
        super().__init__("Дилер")


class Hand:
    def __init__(self):
        self.cards: list[Card] = []

        self.sum = 0
        # Туз может считаться и как 11, и как 1, в зависимости от того, как выгоднее игроку
        self.aces_amount = 0

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

        self.calculate_sum(card)

    def calculate_sum(self, card: Card) -> None:
        value = VALUES[card.rank]
        self.sum += value

        if card.rank == "Туз":
            self.aces_amount += 1

        while self.sum > 21 and self.aces_amount > 0:
            self.sum -= 10
            self.aces_amount -= 1

    @property
    def is_busted(self) -> bool:
        return self.sum > TARGET
