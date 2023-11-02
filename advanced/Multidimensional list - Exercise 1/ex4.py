rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_sum = float('-inf')
max_row = 0
max_column = 0
for i in range(rows - 2):
    for j in range(columns - 2):
        current_sum = 0
        for k in range(i, i + 3):
            for y in range(j, j + 3):
                current_sum += matrix[k][y]
            if current_sum > max_sum:
                max_sum = current_sum
                max_row = i
                max_column = j
print(f"Sum = {max_sum}")
max_submatrix = [matrix[r][max_column:max_column + 3] for r in range(max_row, max_row + 3)]
[print(*row) for row in max_submatrix]
