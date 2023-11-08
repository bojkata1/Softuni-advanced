first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])
n = int(input())
for _ in range(n):
    line = input().split()
    command = line[0] + ' ' + line[1]
    elements = set([int(x) for x in line[2:]])
    if command == 'Add First':
        first_sequence.update(elements)
    elif command == 'Add Second':
        second_sequence.update(elements)
    elif command == 'Remove First':
        first_sequence.difference_update(elements)
    elif command == 'Remove Second':
        second_sequence.difference_update(elements)
    elif command == 'Check Subset':
        print(first_sequence > second_sequence or first_sequence < second_sequence)
first_sequence = map(str, sorted(first_sequence))
second_sequence = map(str, sorted(second_sequence))
print(', '.join(first_sequence))
print(', '.join(second_sequence))
