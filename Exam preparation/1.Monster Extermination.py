from collections import deque
monster_stats = deque(int(x) for x in input().split(","))
soldier_strength = deque(int(x) for x in input().split(","))
killed_monsters = 0
while soldier_strength and monster_stats:
    current_soldier = soldier_strength.pop()
    current_monster = monster_stats.popleft()
    if current_soldier >= current_monster:
        current_soldier -= current_monster
        if not soldier_strength and current_soldier != 0:
            soldier_strength.append(current_soldier)
        elif soldier_strength:
            soldier_strength[-1] += current_soldier
        killed_monsters += 1
    else:
        current_monster -= current_soldier
        monster_stats.append(current_monster)
if not monster_stats:
    print("All monsters have been killed!")
if not soldier_strength:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")
