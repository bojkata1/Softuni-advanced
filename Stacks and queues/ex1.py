list_of_nums = input().split()
new_list = []
for _ in range(len(list_of_nums)):
    new_list.append(list_of_nums.pop())
print(" ".join(new_list))