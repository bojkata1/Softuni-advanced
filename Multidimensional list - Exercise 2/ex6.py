matrix = [[x for x in input()] for _ in range(5)]
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 'A':
            pos = [i, j]
n = int(input())
directions = {'right': [0, 1], 'left': [0, -1], 'up': [-1, 0], 'down': [1, 0]}
for _ in range(n):
    line = input().split()
    if line[0] == 'move':
        pass
    elif line[0] == 'shoot':
        direction = line[1]
        while True:


