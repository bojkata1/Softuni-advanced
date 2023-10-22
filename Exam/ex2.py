def make_move(board, des_row, des_col, position):
    board[position[0]][position[1]] = "-"
    board[des_row][des_col] = "S"
    position = [des_row, des_col]
    return board, position


n = int(input())
board = []
moves = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}
collected_fish = 0
is_sunk = False
for i in range(n):
    board.append(list(input()))
    if "S" in board[i]:
        position = [i, board[i].index("S")]
while True:
    command = input()
    if command == "collect the nets":
        break
    des_row = position[0] + moves[command][0]
    des_col = position[1] + moves[command][1]
    if des_row < 0:
        des_row = n-1
    if des_col < 0:
        des_col = n-1
    if des_row > n-1:
        des_row = 0
    if des_col > n-1:
        des_col = 0

    if board[des_row][des_col] == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{des_row},{des_col}]")
        board, position = make_move(board, des_row, des_col, position)
        is_sunk = True
        collected_fish = 0
        break
    elif board[des_row][des_col].isdigit():
        collected_fish += int(board[des_row][des_col])
    board, position = make_move(board, des_row, des_col, position)
if collected_fish >= 20:
    print("Success! You managed to reach the quota!")
elif not is_sunk:
    print("You didn't catch enough fish and didn't reach the quota! ", end="")
    print(f"You need {20 - collected_fish} tons of fish more.")
if collected_fish:
    print(f"Amount of fish caught: {collected_fish} tons.")
if not is_sunk:
    [print("".join(row)) for row in board]
