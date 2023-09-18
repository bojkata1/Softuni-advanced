from collections import deque
food_quantity = int(input())
orders = deque(map(int, input().split()))
print(max(orders))
while orders:
    if food_quantity - orders[0] < 0:
        break
    else:
        food_quantity -= orders.popleft()
if orders:
    print(f"Orders left: {' '.join(map(str, orders))}")
else:
    print('Orders complete')