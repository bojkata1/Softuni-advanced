n = int(input())
result = set()
for _ in range(n):
    first_pair, second_pair = input().split('-')
    first_start, first_stop = map(int, first_pair.split(','))
    second_start, second_stop = map(int, second_pair.split(','))
    first_set = set(range(first_start, first_stop + 1))
    second_set = set(range(second_start, second_stop + 1))
    if len(first_set & second_set) > len(result):
        result = first_set & second_set
print(f"Longest intersection is [{', '.join(map(str, result))}] with length {len(result)}")
