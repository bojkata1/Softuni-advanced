#user_input = input()
#dict_of_chars = {}
#for char in user_input:
#    if char in dict_of_chars:
#        dict_of_chars[char] += 1
#    else:
#        dict_of_chars[char] = 1
#dict_of_chars = dict(sorted(dict_of_chars.items()))
#for char, count in dict_of_chars.items():
#    print(f"{char}: {count} time/s")
#  po-burzo reshenie


txt = tuple(input())
unique_symbols = sorted(set(txt))
for char in unique_symbols:
    print(f"{char}: {txt.count(char)} time/s")
#  po-bavno reshenie
