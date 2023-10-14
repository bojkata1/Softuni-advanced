print(set('A'))
test_list = ['A', 'B']
print(set(test_list) == {'B', 'A'})

a = [0, 2] * 3
print(a)

b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_b = [num for sublist in b for num in sublist]
print(flat_b)