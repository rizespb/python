from cards import Deck
from constants import DEALER_MIN_TARGET, NO, TARGET
from helpers import (
    ask_to_continue,
    busted,
    game_over,
    input_answer,
    input_bet,
    input_user_name,
)
from player import Dealer, User
from printing import print_card, print_cards


def user_round(user: User, deck: Deck) -> int:
    print("Ваш ход")

    while True:
        user_input = input_answer("Хотите взять карту? (y/n) ")

        if user_input == NO:
            break

        else:
            new_card = deck.get_random_card()

            print("Вы получили карту:")
            print_card(new_card)

            user.hand.add_card(new_card)

            print("Ваши карты:")
            print_cards(user.hand.cards)
            print(f"Текущее количество очков \033[32m{user.hand.sum}\033[0m")

            if user.hand.is_busted:
                break

    result = user.hand.sum

    print(
        f"\nВы завершили раунд.\nКоличество набарнных очков \033[32m{result}\033[0m\n"
    )

    return result


def dealer_round(dealer: Dealer, deck: Deck, user_result: int) -> int:
    print("Ход дилера")

    while True:
        current_sum = dealer.hand.sum

        if current_sum >= DEALER_MIN_TARGET:
            break

        new_card = deck.get_random_card()

        dealer.hand.add_card(new_card)

    print("Карты дилера:")
    print_cards(dealer.hand.cards)

    result = dealer.hand.sum

    print(
        f"Дилер завершил раунд.\nКоличество набранных очков \033[32m{result}\033[0m\n"
    )

    return result


def init_round(user: User, dealer: Dealer, deck: Deck) -> None:
    dealer.init_hand(deck)

    print("\nНачальные карты дилера:")
    print_cards(dealer.hand.cards)
    print(f"Текущее количество очков дилера \033[32m{dealer.hand.sum}\033[0m\n\n")

    user.init_hand(deck)

    print("Ваши начальные карты")
    print_cards(user.hand.cards)
    print(f"Текущее количество Ваших очков \033[32m{user.hand.sum}\033[0m\n\n")


def game() -> None:
    print("Добро пожаловать в игру BackJack!")

    user_name = input_user_name()

    user = User(user_name)
    dealer = Dealer()

    isInGame = True

    while isInGame:
        print("\nНачинаем новый раунд\n")

        print(f"Ваш текущий баланс \033[36m{user.balance}\033[0m")

        bet = input_bet(user.balance)

        deck = Deck()

        init_round(user, dealer, deck)

        user_result = user_round(user, deck)

        if user.hand.is_busted:
            busted()
            user.lost_bet(bet)

            if user.balance <= 0:
                game_over(user.balance)
                break

            isInGame = ask_to_continue(user)
            continue

        if user.hand.sum == TARGET:
            user.win_bet(bet)

            isInGame = ask_to_continue(user)
            continue

        dealer_result = dealer_round(dealer, deck, user_result)

        if dealer.hand.is_busted or user_result >= dealer_result:
            user.win_bet(bet)

            isInGame = ask_to_continue(user)
            continue

        print("Выиграл Дилер")
        user.lost_bet(bet)

        if user.balance <= 0:
            game_over(user.balance)
            break

        isInGame = ask_to_continue(user)


game()
