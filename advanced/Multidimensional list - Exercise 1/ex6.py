rows, columns = [int(x) for x in input().split()]
matrix = [[int(i) for i in input().split()] for _ in range(rows)]
while True:
    command = input()
    if command == 'END':
        break
    command = command.split()
    if len(command) != 5 or command[0] != 'swap':
        print("Invalid input!")
        continue
    else:
        row_first, column_first, row_second, column_second = [int(x) for x in command[1:]]
        if row_first >= rows or row_second >= rows or column_first >= columns or column_second >= columns:
            print("Invalid input!")
            continue
        else:
            temp = matrix[row_first][column_first]
            matrix[row_first][column_first] = matrix[row_second][column_second]
            matrix[row_second][column_second] = temp
            [print(*row) for row in matrix]
