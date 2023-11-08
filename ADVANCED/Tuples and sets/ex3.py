n = int(input())
set_of_elements = set()
for _ in range(n):
    elements = input().split()
    for element in elements:
        set_of_elements.add(element)
print('\n'.join(set_of_elements))
#  print(*set_of_elements, sep='\n')
