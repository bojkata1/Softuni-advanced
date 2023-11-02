from collections import deque
user_input = deque(input().split())
colors = []
main_colors = ['red', 'yellow', 'blue']
secondary_colors = {'orange': ['yellow', 'red'], 'purple': ['red', 'blue'], 'green': ['blue', 'yellow']}
while user_input:
    if len(user_input) == 1:
        if user_input[0] in main_colors or user_input[0] in secondary_colors:
            colors.append(user_input.pop())
            continue
        else:
            user_input.pop()
            continue
    combination = user_input[0] + user_input[-1]
    combination2 = user_input[-1] + user_input[0]
    if combination in main_colors or combination in secondary_colors:
        colors.append(combination)
        user_input.pop()
        user_input.popleft()
    elif combination2 in main_colors or combination2 in secondary_colors:
        colors.append(combination2)
        user_input.pop()
        user_input.popleft()
    else:
        first = user_input.popleft()[:-1]
        second = user_input.pop()[:-1]
        middle_index = len(user_input) // 2
        if len(second) != 0:
            user_input.insert(middle_index, second)
        if len(first) != 0:
            user_input.insert(middle_index, first)
for color in colors:
    if color in secondary_colors:
        if secondary_colors[color][0] not in colors or secondary_colors[color][1] not in colors:
            colors.remove(color)
print(colors)
