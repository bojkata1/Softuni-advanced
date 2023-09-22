from collections import deque
materials_needed = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])
presents = {}
isSuccessful = False
while materials_needed and magic_level:
    total_magic_level = materials_needed[-1] * magic_level[0]
    if materials_needed[-1] == 0:
        materials_needed.pop()
        continue
    if magic_level[0] == 0:
        magic_level.popleft()
        continue
    if total_magic_level == 150:
        if 'Doll' not in presents:
            presents['Doll'] = 0
        presents['Doll'] += 1
        materials_needed.pop()
        magic_level.popleft()
    elif total_magic_level == 250:
        if 'Wooden train' not in presents:
            presents['Wooden train'] = 0
        presents['Wooden train'] += 1
        materials_needed.pop()
        magic_level.popleft()
    elif total_magic_level == 300:
        if 'Teddy bear' not in presents:
            presents['Teddy bear'] = 0
        presents['Teddy bear'] += 1
        materials_needed.pop()
        magic_level.popleft()
    elif total_magic_level == 400:
        if 'Bicycle' not in presents:
            presents['Bicycle'] = 0
        presents['Bicycle'] += 1
        materials_needed.pop()
        magic_level.popleft()
    elif total_magic_level < 0:
        materials_needed.append(materials_needed.pop() + magic_level.popleft())
    else:
        materials_needed[-1] += 15
        magic_level.popleft()
if 'Train' in presents and 'Doll' in presents:
    isSuccessful = True
if 'Teddy bear' in presents and 'Bicycle' in presents:
    isSuccessful = True
print(f'{"The presents are crafted! Merry Christmas!" if isSuccessful else "No presents this Christmas!"}')
if materials_needed:
    print('Materials left: ', end='')
    while materials_needed:
        if len(materials_needed) > 1:
            print(materials_needed.pop(), end=', ')
        else:
            print(materials_needed.pop())
if magic_level:
    print('Magic left: ', end='')
    while magic_level:
        if len(magic_level) > 1:
            print(magic_level.popleft(), end=', ')
        else:
            print(magic_level.popleft())
presents = dict(sorted(presents.items()))
for item, count in presents.items():
    print(f'{item}: {count}')
