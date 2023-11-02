stack = [int(x) for x in input().split()]
rack_capacity = int(input())
counter = 0
while stack:
    current_capacity = rack_capacity
    counter += 1
    while stack and current_capacity >= stack[-1]:
        current_capacity -= stack.pop()
print(counter)
