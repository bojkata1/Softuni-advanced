n = int(input())
matrix = []
for i in range(n):
    elements = [x for x in input().split(', ')]
    matrix.append(elements)
prime_diagonal = []
prime_sum = 0
secondary_diagonal = []
secondary_sum = 0
for i in range(n):
    for j in range(n):
        if i == j:
            prime_diagonal += matrix[i][j]
            prime_sum += int(matrix[i][j])
        if (i + j) == (n - 1):
            secondary_diagonal += matrix[i][j]
            secondary_sum += int(matrix[i][j])
print(f"Primary diagonal: {', '.join(prime_diagonal)}. Sum: {prime_sum}")
print(f"Secondary diagonal: {', '.join(secondary_diagonal)}. Sum: {secondary_sum}")
