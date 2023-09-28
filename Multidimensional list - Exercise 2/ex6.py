matrix = [[x for x in input().split()] for _ in range(5)]
target_count = 0
targets_hit = []
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 'A':
            pos = [i, j]
        if matrix[i][j] == 'x':
            target_count += 1
n = int(input())
directions = {'right': [0, 1], 'left': [0, -1], 'up': [-1, 0], 'down': [1, 0]}
for _ in range(n):
    line = input().split()
    direction = line[1]
    if line[0] == 'move':
        steps = int(line[2])
        fut_pos = [pos[0] + (steps * directions[direction][0]), pos[1] + (steps * directions[direction][1])]
        if 0 <= fut_pos[0] < 5 and 0 <= fut_pos[1] < 5 and matrix[fut_pos[0]][fut_pos[1]] == '.':
            pos[0] += steps * directions[direction][0]
            pos[1] += steps * directions[direction][1]
    elif line[0] == 'shoot':
        r = pos[0] + directions[direction][0]
        c = pos[1] + directions[direction][1]
        while 0 <= r < 5 and 0 <= c < 5:
            if matrix[r][c] == 'x':
                target_count -= 1
                matrix[r][c] = '.'
                targets_hit.append([r, c])
                break
            r += directions[direction][0]
            c += directions[direction][1]
        if target_count == 0:
            break
if target_count:
    print(f'Training not completed! {target_count} targets left.')
else:
    print(f'Training completed! All {len(targets_hit)} targets hit.')
if targets_hit:
    [print(row) for row in targets_hit]
