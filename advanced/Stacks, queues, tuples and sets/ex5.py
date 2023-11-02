from collections import deque
materials_needed = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])
presents = {}
items = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}
isSuccessful = False
while materials_needed and magic_level:
    total_magic_level = materials_needed[-1] * magic_level[0]
    if materials_needed[-1] == 0 and magic_level[0] == 0:
        materials_needed.pop()
        magic_level.popleft()
        continue
    if materials_needed[-1] == 0:
        materials_needed.pop()
        continue
    if magic_level[0] == 0:
        magic_level.popleft()
        continue
    if total_magic_level in items:
        if items[total_magic_level] not in presents:
            presents[items[total_magic_level]] = 0
        presents[items[total_magic_level]] += 1
        materials_needed.pop()
        magic_level.popleft()
    elif total_magic_level < 0:
        materials_needed.append(materials_needed.pop() + magic_level.popleft())
    elif total_magic_level > 0:
        materials_needed[-1] += 15
        magic_level.popleft()
if ('Wooden train' in presents and 'Doll' in presents) or ('Teddy bear' in presents and 'Bicycle' in presents):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
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
