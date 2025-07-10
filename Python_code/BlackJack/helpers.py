from typing import Tuple

from constants import NO, VALID_ANSWERS
from player import User


def input_user_name() -> str:

    player_name = None

    while not player_name:
        user_input = input(("Как вас зовут? ")).strip()

        if user_input:
            player_name = user_input
        else:
            print("Имя не должно быть пустым")

    return player_name


def input_answer(
    question: str,
    valid_answers: Tuple[str, ...] = VALID_ANSWERS,
    fallback: str | None = None,
) -> str:
    answer = None

    while not answer:
        user_input = input(question).strip().lower()

        if not user_input in valid_answers:
            if fallback:
                print(fallback)

            continue

        else:
            answer = user_input
            break

    return answer


def input_bet(balance) -> int:
    bet = None

    while not bet:
        user_input = input(f"Введите ставку от 1 до {balance}: ")

        try:
            value = int(user_input)

            if value <= 0 or value > balance:
                raise Exception("Incorrect input")
        except:
            print("Вы ввели некорректное значение")
        else:
            bet = value
            break

    return bet


def game_over(balance: int) -> None:
    print(f"Ваш баланс {balance}$. Вы проиграли. Хорошего вечера")


def busted() -> None:
    print("Перебор))")


def ask_to_continue(user: User) -> bool:
    user_input = input_answer("Желаете сыграть еще? ")

    if user_input == NO:
        print(f"\nВаш баланс {user.balance}$. Игра окончена. Хорошего вечера!")
        return False

    return True
