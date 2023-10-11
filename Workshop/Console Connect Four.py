from collections import deque


class InvalidColumn(Exception):
    pass


def display(mat):
    for element in mat:
        print(element)
    print()


def place(mat, col, player):
    for i in range(ROWS):
        if mat[i][col] != 0:
            mat[i-1][col] = player
            break
        elif i == ROWS-1:
            mat[i][col] = player
            break
    return mat


def is_winner(mat, player):
    diagonal_moves = [(1, 1), (2, 2), (3, 3)]
    horizontal_moves = [(0, 1), (0, 2), (0, 3)]
    vertical_moves = [(1, 0), (2, 0), (3, 0)]
    for i in range(ROWS):
        for j in range(COLUMNS):
            counter = 1
            if mat[i][j] == player:
                try:
                    for move in diagonal_moves:
                        if mat[i+move[0]][j+move[1]] == player:
                            counter += 1
                    if counter >= 4:
                        return True
                except IndexError:
                    pass
                try:
                    for move in diagonal_moves:
                        if mat[i-move[0]][j+move[1]] == player:
                            counter += 1
                    if counter >= 4:
                        return True
                except IndexError:
                    pass
                try:
                    counter = 1
                    for move in horizontal_moves:
                        if mat[i+move[0]][j+move[1]] == player:
                            counter += 1
                    if counter >= 4:
                        return True
                except IndexError:
                    pass
                try:
                    counter = 1
                    for move in vertical_moves:
                        if mat[i+move[0]][j+move[1]] == player:
                            counter += 1
                    if counter >= 4:
                        return True
                except IndexError:
                    pass
    return False


ROWS = 6
COLUMNS = 7
mat = [[0] * COLUMNS for _ in range(ROWS)]
player = deque([1, 2, 3])
while True:
    print(f"Player {player[0]}, please choose a column")
    col = int(input())
    if col > COLUMNS-1:
        raise InvalidColumn
    mat = place(mat, col, player[0])
    display(mat)
    if is_winner(mat, player[0]) is True:
        print(f"The winner is {player[0]}")
        break
    player.append(player.popleft())
