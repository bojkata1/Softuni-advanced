from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances and challenges:
    current_tool = tools.popleft()
    current_substance = substances.pop()
    combo = current_tool * current_substance
    if combo in challenges:
        challenges.remove(combo)
    else:
        tools.append(current_tool + 1)
        if current_substance - 1 != 0:
            substances.append(current_substance-1)
if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
if tools:
    print(f"Tools: {', '.join([str(x) for x in tools])}")
if substances:
    print(f"Substances: {', '.join([str(x) for x in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")
