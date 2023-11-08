n = int(input())
even = set()
odd = set()
for i in range(1, n + 1):
    char_sum = sum([ord(char) for char in input()]) // i
    if char_sum % 2 == 0:
        even.add(char_sum)
    elif char_sum % 2 != 0:
        odd.add(char_sum)
sum_of_even = sum(even)
sum_of_odd = sum(odd)
if sum_of_even == sum_of_odd:
    result = odd | even
elif sum_of_even < sum_of_odd:
    result = odd - even
elif sum_of_even > sum_of_odd:
    result = odd ^ even
print(*result, sep=', ')
