rows, columns = [int(x) for x in input().split()]
matrix = []
max_sum = 0
for i in range(rows):
    matrix.append([int(x) for x in input().split()])
for i in range(rows):
    for j in range(columns):
        current_sum = 0
        for k in range(i - 3, i):
            for y in range(j - 3, j):
                current_sum += matrix[k][y]
                if current_sum > max_sum:
                    max_sum = current_sum
                    row = i - 3
                    column = j - 3
print(f"Sum = {max_sum}")
for i in range(row, row + 3):
    for j in range(column, column + 3):
        print(matrix[i][j], end=' ')
    print()
