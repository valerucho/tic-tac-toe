board = list(range(1, 10))


def draw_board():
    print("――――――――")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
    print("――――――――")


def input_symbol(cross_or_zero):
    while True:
        answer = input("В какую ячейку поставить " + cross_or_zero + "? ")
        answer = int(answer)
        if answer not in range(1, 10):
            print("В игре всего 9 клеток")
            continue
        if str(board[answer - 1]) in "XO":
            print("Ячейка уже занята")
            continue
        board[answer - 1] = cross_or_zero
        break


def check_win():
    win = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (2, 5, 8), (1, 4, 7), (3, 6, 9), (7, 5, 3), (9, 5, 1)]
    for each in win:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            input_symbol("X")
        else:
            input_symbol("O")
        counter += 1
        if counter > 4:
            winner = check_win()
            if winner:
                draw_board()
                print("")
                print(winner, "Выиграл!")
            break
        if counter == 9:
            draw_board()
            print("Ничья!")
            break


main()
