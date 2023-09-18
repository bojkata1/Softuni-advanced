stack = []
n = int(input())
for _ in range(n):
    user_input = input().split()
    if user_input[0] == '1':
        stack.append(int(user_input[1]))
    elif stack:
        if user_input[0] == '2':
            stack.pop()
        elif user_input[0] == '3':
            print(max(stack))
        elif user_input[0] == '4':
            print(min(stack))
while stack:
    print(stack.pop(), end="")
    if stack:
        print(", ", end="")