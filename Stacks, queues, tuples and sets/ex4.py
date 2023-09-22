from collections import deque
working_bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
honey = 0

operator = {
    '+': lambda a, b: abs(a + b),
    '-': lambda a, b: abs(a - b),
    '/': lambda a, b: abs(a / b),
    '*': lambda a, b: abs(a * b)
}

while working_bees and nectar:
    if symbols[0] == '/' and nectar[-1] <= 0:
        symbols.popleft()
        working_bees.popleft()
        nectar.pop()
        continue
    if working_bees[0] <= nectar[-1]:
        honey += operator[symbols.popleft()](working_bees.popleft(), nectar.pop())
    else:
        nectar.pop()
        continue
print(f"Total honey made: {honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
