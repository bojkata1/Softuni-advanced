from collections import deque
chocolate = list(map(int, input().split(', ')))
cups_of_milk = deque(map(int, input().split(', ')))
milk_shakes = 0
while chocolate and cups_of_milk and milk_shakes < 5:
    if milk_shakes == 5:
        break
    if cups_of_milk[0] <= 0 and chocolate[-1] <= 0:
        cups_of_milk.popleft()
        chocolate.pop()
        continue
    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue
    if chocolate[-1] <= 0:
        chocolate.pop()
        continue
    if chocolate[-1] == cups_of_milk[0]:
        chocolate.pop()
        cups_of_milk.popleft()
        milk_shakes += 1
    else:
        chocolate[-1] -= 5
        cups_of_milk.rotate(-1)
if milk_shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print(f"Chocolate: {', '.join([str(x) for x in chocolate]) if chocolate else 'empty'}")
print(f"Milk: {', '.join(map(str, cups_of_milk)) if cups_of_milk else 'empty'}")
