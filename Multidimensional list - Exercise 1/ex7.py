rows, columns = [int(x) for x in input().split()]
snake = input()
matrix = []
index = 0
isReverse = False
for i in range(rows):
    matrix.append([])
    for j in range(columns):
        matrix[i].append(snake[index])
        index += 1
        if index == len(snake):
            index = 0
for i in range(rows):
    if not isReverse:
        print(''.join(matrix[i]))
        isReverse = True
    else:
        print(''.join(reversed(matrix[i])))
        isReverse = False
