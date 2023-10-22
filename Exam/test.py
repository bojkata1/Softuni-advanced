a  = {x: 0 for x in [1, 2, 3]}
print(a)
b = {x for x in [1, 2, 3]}
print(b)

c = [x if x == "e" else -1 for x in "sometext"]
print(c)

d = {1, 1, 2, 3, 6, 7}
print(d)