def make_move(matrix, row, col, prev_row, prev_col):
    matrix[row][col] = "s"
    matrix[prev_row][prev_col] = "*"
    return matrix, [row, col]


is_interrupted = False
nuts = 0
collected = 0
n = int(input())
commands = input().split(", ")
matrix = [list(input()) for _ in range(n)]
moves = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}
for i in range(n):
    row = ''.join(matrix[i])
    if "s" in row:
        position = [i, row.index("s")]
        break
    nuts += row.count("h")
for command in commands:
    desired_row = position[0] + moves[command][0]
    desired_col = position[1] + moves[command][1]
    if desired_col >= n or desired_col < 0 or desired_row >= n or desired_row < 0:
        print("The squirrel is out of the field.")
        is_interrupted = True
        break
    if matrix[desired_row][desired_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        matrix, position = make_move(matrix, desired_row, desired_col, position[0], position[1])
        is_interrupted = True
        break
    if matrix[desired_row][desired_col] == "h":
        collected += 1
        nuts -= 1
        matrix, position = make_move(matrix, desired_row, desired_col, position[0], position[1])
        if collected == 3:
            print("Good job! You have collected all hazelnuts!")
            is_interrupted = True
            break
    if matrix[desired_row][desired_col] == "*":
        matrix, position = make_move(matrix, desired_row, desired_col, position[0], position[1])
if nuts != 0 and not is_interrupted:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {collected}")
