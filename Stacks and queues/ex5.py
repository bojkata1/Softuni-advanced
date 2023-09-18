from collections import deque
number_of_petrol_pumps = int(input())
queue = deque()
start_position = 0
stops = 0
for _ in range(number_of_petrol_pumps):
    petrol_amount, distance_from_pumps = map(int, input().split())
    queue.append([petrol_amount, distance_from_pumps])
while stops < number_of_petrol_pumps:
    fuel = 0
    for i in range(number_of_petrol_pumps):
        fuel += queue[i][0] - queue[i][1]
        if fuel < 0:
            queue.rotate(-1)
            start_position += 1
            stops = 0
            break
    stops += 1
print(start_position)
