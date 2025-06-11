from random import randint


def get_players_symbols():
    players_map = {}

    player1 = None
    player2 = None

    while player1 not in ["X", "O"]:
        print("Игрок 1: Кем вы хотите играть: X или O?")
        player1 = input()

        player2 = "O" if player1 == "X" else "X"

    players_map[1] = player1
    players_map[2] = player2

    return players_map


def input_num(player, symbol):
    while True:
        print(
            f"Игрок {player}, выберите следующую ячейку (1 - 9), где будет размещен {symbol}"
        )

        digit = input()

        if digit.isdigit() and 1 <= int(digit) <= 9:
            return int(digit)
        else:
            print("Вы ввели некорректное число. Попробуйте снова.\n")
            continue


def print_board(board=[]):
    def print_line(c1=" ", c2=" ", c3=" "):
        print(" {} | {} | {} ".format(c1, c2, c3))

    for line in range(2, -1, -1):
        c1 = board[line * 3 + 1] or " "
        c2 = board[line * 3 + 2] or " "
        c3 = board[line * 3 + 3] or " "

        print_line()
        print_line(c1, c2, c3)
        print_line()
        line != 0 and print("-----------")
    else:
        print("\n")


def is_win(board):
    for num in range(0, 3):
        row1 = num * 3 + 1
        row2 = row1 + 1
        row3 = row2 + 1

        column1 = num + 1
        column2 = column1 + 3
        column3 = column2 + 3

        if (
            board[row1] == board[row2] == board[row3] != False
            or board[column1] == board[column2] == board[column3] != False
        ):
            return True

    if (
        board[1] == board[5] == board[9] != False
        or board[7] == board[5] == board[3] != False
    ):
        return True

    return False


is_draw = lambda board: all(board[1:])


def congratulation(player):
    print(f"Игрок {player} победил. Игра окончена. Поздравляем!")


def initGame():
    # "Non-used cell" не используется, создана для того, чтобы цифры 1-9 на клавиатуре соответствовали индексам в board
    board = ["Non-used cell"] + [False] * 9

    print_board(board)
    print("Добро пожаловать в игру Крестики-Нолики!\n")

    # Словарь того, какой символ соответствует какому игроку
    players_map = get_players_symbols()

    current_player = randint(1, 2)

    print(f"\nНачинает Игрок {current_player}\n")

    isFinished = False

    return {
        "board": board,
        "players_map": players_map,
        "current_player": current_player,
        "isFinished": isFinished,
    }


def game():
    # board, players_map, current_player, isFinished = initGame()
    initial = initGame()
    board, players_map, current_player, isFinished = (
        initial["board"],
        initial["players_map"],
        initial["current_player"],
        initial["isFinished"],
    )
    print(board)

    board = initial["board"]
    players_map = initial["players_map"]
    current_player = initial["current_player"]
    isFinished = initial["isFinished"]

    while not isFinished:
        current_symbol = players_map[current_player]

        cell_number = input_num(current_player, current_symbol)

        # Если выбранная ячейка свободна
        if not board[cell_number]:
            board[cell_number] = current_symbol
            print_board(board)
            print(board)

            is_current_win = is_win(board)

            if is_current_win:
                congratulation(current_player)
                break
            elif is_draw(board):
                print(
                    "Ничья. Игра окончена. Вы можете сыграть еще раз. Сыграем? (yes / no)"
                )

                answer = input()

                if answer == "yes":
                    initial = initGame()
                    board, players_map, current_player, isFinished = (
                        initial["board"],
                        initial["players_map"],
                        initial["current_player"],
                        initial["isFinished"],
                    )
                    continue
                else:
                    break

            else:
                current_player = 3 - current_player
                continue
        else:
            print("Эта ячейка уже занята. Выберите другую\n")
            continue


game()
