from collections import deque
from math import floor
user_input = input().split()
stack = deque()
result = 0
isFirstVar = True
for char in user_input:
    if stack and isFirstVar is True:
        if isFirstVar:
            result = stack.popleft()
            isFirstVar = False
    if char == '+':
        while stack:
            result += stack.popleft()
    elif char == '-':
        while stack:
            result -= stack.popleft()
    elif char == '*':
        while stack:
            result *= stack.popleft()
    elif char == '/':
        while stack:
            result /= stack.popleft()
            result = floor(result)
    else:
        stack.append(int(char))
print(result)