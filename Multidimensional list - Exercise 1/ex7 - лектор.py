from collections import deque
r, c = [int(x) for x in input().split()]
txt = deque(input())
matrix = []
for row in range(r):
    matrix.append([''] * c)
    for column in range(c):
        if row % 2 == 0:
            matrix[row][column] = txt[0]
        else:
            matrix[row][-1 - column] = txt[0]
        txt.rotate(-1)
[print(*row, sep='') for row in matrix]
