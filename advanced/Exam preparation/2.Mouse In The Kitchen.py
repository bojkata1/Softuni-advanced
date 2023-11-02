n, m = [int(x) for x in input().split(',')]
cupboard = [list(input()) for _ in range(n)]
moves = {'up': (-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1)}
cheese = 0
for i in range(n):
        if 'M' in cupboard[i]:
            mouse_pos = [i, cupboard[i].index('M')]
        cheese += cupboard[i].count('C')
while True:
    command = input()
    if command == 'danger':
        print("Mouse will come back later!")
        break
    desired_row = mouse_pos[0] + moves[command][0]
    desired_col = mouse_pos[1] + moves[command][1]
    try:
        if cupboard[desired_row][desired_col] == '@':
            continue
        if cupboard[desired_row][desired_col] == 'T':
            print("Mouse is trapped!")
            cupboard[mouse_pos[0]][mouse_pos[1]] = '*'
            cupboard[desired_row][desired_col] = 'M'
            mouse_pos = [desired_row, desired_col]
            break
        if cupboard[desired_row][desired_col] == 'C':
            cheese -= 1
            cupboard[mouse_pos[0]][mouse_pos[1]] = '*'
            cupboard[desired_row][desired_col] = 'M'
            mouse_pos = [desired_row, desired_col]
            if cheese == 0:
                print("Happy mouse! All the cheese is eaten, good night!")
                break
        else:
            cupboard[mouse_pos[0]][mouse_pos[1]] = '*'
            cupboard[desired_row][desired_col] = 'M'
            mouse_pos = [desired_row, desired_col]
    except IndexError:
        print("No more cheese for tonight!")
        break
for row in cupboard:
    print(*row, sep='')
