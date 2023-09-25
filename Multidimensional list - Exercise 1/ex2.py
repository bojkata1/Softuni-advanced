matrix = []
n = int(input())
prime_sum = 0
secondary_sum = 0
for i in range(n):
    elements = [int(x) for x in input().split()]
    matrix.append(elements)
for i in range(n):
    for j in range(n):
        if i == j:
            prime_sum += matrix[i][j]
        if (i + j) == (n - 1):
            secondary_sum += matrix[i][j]
result = prime_sum - secondary_sum
print(abs(result))
