n = int(input())
matrix = []
knights = []
removed_knights = 0

for row in range(n):
    matrix.append([x for x in input()])
    for col in range(n):
        if matrix[row][col] == 'K':
            knights.append([row, col])

possible_moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (1, 2), ]
while True:
    for knight in knights:
        for i, j in possible_moves:
            if [knight[0] + i, knight[1] + j] in knights:
                knights.remove([knight[0] + i, knight[1] + j])
                removed_knights += 1
                continue
    break
print(removed_knights)