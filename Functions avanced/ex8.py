def age_assignment(*args, **kwargs):
    result = []
    new_dict = {}
    for key, value in kwargs.items():
        for name in args:
            if name.startswith(key):
                new_dict[name] = value
    sorted_new_dict = dict(sorted(new_dict.items(), key=lambda kvp: kvp[0]))
    for key, value in sorted_new_dict.items():
        result.append(f'{key} is {value} years old.')
    return '\n'.join(result)

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))