rows, columns = [int(x) for x in input().split()]
start = ord('a')

for row in (range(rows)):
    for column in range(columns):
        print(f'{chr(start + row)}{chr(start + row + column)}{chr(start + row)}', end=' ')
    print()