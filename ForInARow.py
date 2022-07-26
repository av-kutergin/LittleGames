import sys

columns = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
}
player_X = 'X'
player_O = 'O'


def draw_board():
    num_row = ' 1234567\n'
    border = '+-------+'
    print(num_row + border)
    for i in range(5, -1, -1):
        row = '+'
        for key, value in columns.items():
            if i >= len(value):
                row += '.'
            else:
                row += str(value[i])
        row += '+'
        print(row)
    print(border)
    print(num_row)


def get_next_move(player):
    row = input(f'Player {player} Choose your column: ')
    if row == 'QUIT':
        print('See you soon!')
        return sys.exit()
    if row not in ('1', '2', '3', '4', '5', '6', '7'):
        print('Wrong input, try again')
        return get_next_move(player)
    if len(columns[int(row)]) == 6:
        print('Column is full, try again')
        return get_next_move(player)
    columns[int(row)].append(player)
    draw_board()
    win = check_win(player, int(row))
    if win:
        print(f'Player {player} WON!')
        return sys.exit()
    return


def check_win(player, row):
    horizontal_match = 1
    vertical_match = 1
    diagonal_upward_match = 1
    diagonal_downward_match = 1
    index = len(columns[row]) - 1

    # check match on the left
    if row > 1:
        # check horizontal
        for i in range(1, row):
            column_to_check = columns[row-i]
            if (index >= len(column_to_check)) or (column_to_check[index] != player):
                break
            horizontal_match += 1

        # check diagonal upward
        for i in range(1, row):
            column_to_check = columns[row - i]
            if (index-i < 0) or (index-i >= len(column_to_check)) or (column_to_check[index-i] != player):
                break
            diagonal_upward_match += 1

        # check diagonal downward
        for i in range(1, row):
            column_to_check = columns[row - i]
            if (index + i >= len(column_to_check)) or (column_to_check[index+i] != player):
                break
            diagonal_downward_match += 1

    # check match on the right
    if row < 7:
        # check horizontal
        for i in range(1, 8-row):
            column_to_check = columns[row + i]
            if (index >= len(column_to_check)) or (player != column_to_check[index]):
                break
            horizontal_match += 1

        # check diagonal upward
        for i in range(1, 8 - row):
            column_to_check = columns[row + i]
            if (index + i >= len(column_to_check)) or (column_to_check[index+i] != player):
                break
            diagonal_upward_match += 1

        # check diagonal downward
        for i in range(1, 8 - row):
            column_to_check = columns[row + i]
            if (index - i < 0) or (index - i >= len(column_to_check)) or (column_to_check[index-i] != player):
                break
            diagonal_downward_match += 1

    if len(columns[row]) >= 4:
        # check match below
        for i in range(1, index+1):
            if player != columns[row][index-i]:
                break
            vertical_match += 1

    if (
            vertical_match == 4
            or horizontal_match == 4
            or diagonal_upward_match == 4
            or diagonal_downward_match == 4
    ):
        return True
    return False


def game():
    draw_board()
    move_counter = 0
    player = player_O
    while True:
        player = player_O if player == player_X else player_X
        get_next_move(player)
        move_counter += 1


if __name__ == "__main__":
    game()
