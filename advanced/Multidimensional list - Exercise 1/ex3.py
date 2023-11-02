rows, columns = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]
count = 0
for i in range(rows-1):
    for j in range(columns-1):
        element = matrix[i][j]
        if element == matrix[i][j+1] and element == matrix[i+1][j] and element == matrix[i+1][j+1]:
            count += 1
print(count)
