from collections import deque

fuel = [int(x) for x in input().split()]
consumption_indexes = deque(int(x) for x in input().split())
fuel_needed = deque(int(x) for x in input().split())
altitude_number = 0
reached_altitudes = []
while fuel and consumption_indexes and fuel_needed:
    fuel_used = fuel[-1] - consumption_indexes[0]
    current_altitude = fuel_needed[0]
    if fuel_used >= current_altitude:
        altitude_number += 1
        fuel.pop()
        consumption_indexes.popleft()
        fuel_needed.popleft()
        print(f"John has reached: Altitude {altitude_number}")
        reached_altitudes.append(f"Altitude {altitude_number}")
    else:
        print(f"John did not reach: Altitude {altitude_number+1}")
        break
if altitude_number != 0 and fuel_needed:
    print("John failed to reach the top.\nReached altitudes: ", end="")
    print(", ".join(reached_altitudes))
elif altitude_number == 0:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
if altitude_number != 0 and not fuel_needed:
    print("John has reached all the altitudes and managed to reach the top!")
