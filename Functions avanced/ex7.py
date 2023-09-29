def grocery_store(**kwargs):
    result = []
    sorted_dict = dict(sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0])))
    for key, value in sorted_dict.items():
        result.append(f'{key}: {value}')
    return '\n'.join(result)


print(grocery_store(
        bread=5,
        pasta=12,
        eggs=12,
    ))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
