m = int(input())
n = int(input())
matrix = []
nice_kids_count = 0
nice_kids_presents = 0
moves = {'right': (0, 1), 'left': (0, -1), 'up': (-1, 0), 'down': (1, 0)}
for i in range(n):
    matrix.append(input().split())
    for j in range(n):
        if matrix[i][j] == 'S':
            pos = [i, j]
        if matrix[i][j] == 'V':
            nice_kids_count += 1
while m > 0:
    if nice_kids_count == 0:
        break
    command = input()
    if command == 'Christmas morning':
        break
    r = pos[0] + moves[command][0]
    c = pos[1] + moves[command][1]
    if 0 <= r < n and 0 <= c < n:
        matrix[pos[0]][pos[1]] = '-'
        pos[0] = r
        pos[1] = c
    if matrix[r][c] == 'V':
        m -= 1
        nice_kids_count -= 1
        nice_kids_presents += 1
    if matrix[r][c] == 'C':
        for directions, move in moves.items():
            if matrix[r+move[0]][c+move[1]] == 'X' or matrix[r+move[0]][c+move[1]] == 'V':
                m -= 1
                if matrix[r+move[0]][c+move[1]] == 'V':
                    nice_kids_count -= 1
                    nice_kids_presents += 1
                matrix[r + move[0]][c + move[1]] = '-'
    matrix[pos[0]][pos[1]] = 'S'

if nice_kids_count != 0 and m == 0:
    print("Santa ran out of presents!")
[print(*row) for row in matrix]
if nice_kids_count == 0:
    print(f'Good job, Santa! {nice_kids_presents} happy nice kid/s.')
else:
    print(f"No presents for {nice_kids_count} nice kid/s.")