def is_valid_sign(player_one_sign_):
    return player_one_sign_ in ['X', 'O']


def render_board(board_):
    for row in board_:
        print("| ", end="")
        print(" | ".join([sign if sign else " " for sign in row]), end="")
        print(" |")


def is_row_win(board_):
    for row in board_:
        if len(set(row)) == 1 and set(row) != {None}:
            return True
    return False


def is_column_win(board_, current_sign_):
    for col in range(len(board_)):
        current_column = []
        for row in range(len(board_)):
            current_column.append(board_[row][col] == current_sign_)
        if all(current_column):
            return True
    return False


def is_diagonal_win(board_, current_sign_):
    diagonal_1, diagonal_2 = [], []
    for index in range(len(board_)):
        diagonal_1.append(board_[index][index] == current_sign_)
        diagonal_2.append(board_[index][len(board_) - 1 - index] == current_sign_)
    return any([all(diagonal_1), all(diagonal_2)])


def is_win(board_, current_sign_):
    return any([is_row_win(board_), is_column_win(board_, current_sign_), is_diagonal_win(board_, current_sign_)])


def is_draw(board_):
    if any([is_row_win_possible(board_), is_col_win_possible(board_), is_diagonal_win_possible(board_)]):
        return False
    return True


def is_valid_choice(board_, board_mapper_, choice_):
    if not choice_.isdigit():
        return False
    choice_ = int(choice_)
    if choice_ not in board_mapper_:
        return False
    row, col = board_mapper_[choice_]
    return board_[row][col] is None


def is_row_win_possible(board_):
    if all('X' in row_ and 'O' in row_ for row_ in board_):
        return False
    return True


def is_col_win_possible(board_):
    columns = []
    for col_ in range(len(board_)):
        current_col = []
        for row_ in range(len(board_)):
            current_col.append(board_[row_][col_])
        columns.append(current_col)
    if all('X' in col_ and 'O' in col_ for col_ in columns):
        return False
    return True


def is_diagonal_win_possible(board_):
    diagonal_1 = []
    diagonal_2 = []
    for index in range(len(board_)):
        diagonal_1.append(board_[index][index])
        diagonal_2.append(board_[index][len(board_) - 1 - index])
    if 'X' in diagonal_1 and 'O' in diagonal_1 and 'X' in diagonal_2 and 'O' in diagonal_2:
        return False
    return True

player_one = input("Player one: ").strip()
player_two = input("Player two: ").strip()


while True:
    player_one_sign = input(f"{player_one}, would you like to play with 'X' or 'O'? ")
    if is_valid_sign(player_one_sign):
        break
    print("Please, enter 'X' or 'O'!")

player_two_sign = 'X' if player_one_sign != 'X' else 'O'

print("This is the numberation of the board:")

size = 3
board = [[None] * size for _ in range(size)]
board_mapper = {i + 1: (i // size, i % size) for i in range(size ** 2)}

[print(f"| {' | '.join([str(i + 1 + row * size) for i in range(size)])} |") for row in range(size)]
print(f"{player_one} starts first")

turn = 1

while True:
    current_player = player_one if turn % 2 != 0 else player_two
    current_sign = player_one_sign if turn % 2 != 0 else player_two_sign
    while True:
        choice = input(f"{current_player}, choose a free position [1-{size ** 2}]: ").strip()
        if is_valid_choice(board, board_mapper, choice):
            break
        else:
            print("This position is already taken")
    row, col = board_mapper[int(choice)]
    board[row][col] = current_sign
    render_board(board)
    if is_win(board, current_sign):
        print(f"{current_player} won!")
        break
    if is_draw(board):
        print("Draw!")
        break
    turn += 1
