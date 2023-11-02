letters = 'abcdefghijklmnopqrstuvwxyz'
rows, columns = [int(x) for x in input().split()]
letter_index = 0
matrix = []
for i in range(rows):
    word = ''
    for j in range(letter_index, columns + letter_index):
            word += letters[letter_index] + letters[j] + letters[letter_index] + ' '
    letter_index += 1
    matrix.append(word.split())
[print(*row) for row in matrix]
