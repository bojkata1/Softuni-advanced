n = int(input())
matrix = [[x for x in input().split()] for _ in range(n)]
r, c = 0, 0
max_eggs = float('-inf')
eggs = 0
route = []
temp = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'B':
            r = i
            c = j

for right in range(c+1, n):
    if matrix[r][right] == 'X':
        break
    eggs += int(matrix[r][right])
    temp.append([r, right])
if eggs > max_eggs:
    max_eggs = eggs
    route = temp.copy()
    direction = 'right'
temp.clear()
eggs = 0
for left in range(c-1, -1, -1):
    if matrix[r][left] == 'X':
        break
    eggs += int(matrix[r][left])
    temp.append([r, left])
if eggs > max_eggs:
    max_eggs = eggs
    route = temp.copy()
    direction = 'left'
temp.clear()
eggs = 0
for up in range(r-1, -1, -1):
    if matrix[up][c] == 'X':
        break
    eggs += int(matrix[up][c])
    temp.append([up, c])
if eggs > max_eggs:
    max_eggs = eggs
    route = temp.copy()
    direction = 'up'
temp.clear()
eggs = 0
for down in range(r + 1, n):
    if matrix[down][c] == 'X':
        break
    eggs += int(matrix[down][c])
    temp.append([down, c])
if eggs > max_eggs:
    max_eggs = eggs
    route = temp.copy()
    direction = 'down'
print(direction)
[print(row) for row in route]
print(max_eggs)
