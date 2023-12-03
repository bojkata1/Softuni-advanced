import itertools


def possible_permutations(ls):
    for perm in itertools.permutations(ls):
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]