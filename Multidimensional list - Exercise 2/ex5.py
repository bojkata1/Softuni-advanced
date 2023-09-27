n = int(input())
matrix = [[x for x in input().split()] for _ in range(n)]
tea_bags = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'A':
            pos = [i, j]
        if matrix[i][j] == 'R':
            rabbit_hole = [i, j]
matrix[pos[0]][pos[1]] = '*'
while True:
    if tea_bags >= 10:
        break
    command = input()
    if command == 'right':
        pos[1] += 1
    elif command == 'left':
        pos[1] -= 1
    elif command == 'down':
        pos[0] += 1
    elif command == 'up':
        pos[0] -= 1
    x, y = pos
    if 0 <= x < n and 0 <= y < n:
        if matrix[x][y] == 'R':
            matrix[x][y] = '*'
            break
        if matrix[x][y] != '.' and matrix[x][y] != '*':
            tea_bags += int(matrix[x][y])
        matrix[x][y] = '*'
    else:
        break
if tea_bags == 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
[print(*row) for row in matrix]
