rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
while True:
    line = input().split()
    command = line[0]
    if command == 'END':
        break
    row, col = int(line[1]), int(line[2])
    if 0 <= row < rows and 0 <= col < rows:
        number = int(line[3])
        if command == 'Add':
            matrix[row][col] += number
        elif command == 'Subtract':
            matrix[row][col] -= number
    else:
        print('Invalid coordinates')
[print(*row) for row in matrix]
