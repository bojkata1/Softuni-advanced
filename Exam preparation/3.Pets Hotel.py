def accommodate_new_pets(capacity, max_weight, *args):
    number_of_pets = len(args)
    pets = {}
    for pet, weight in args:
        if capacity == 0:
            break
        number_of_pets -= 1
        if max_weight < weight:
            continue
        if pet not in pets.keys():
            pets[pet] = 0
        pets[pet] += 1
        capacity -= 1
    pets = dict(sorted(pets.items(), key=lambda kvp: kvp[0]))
    if number_of_pets == 0:
        result = f"All pets are accommodated! Available capacity: {capacity}.\n"
    else:
        result = "You did not manage to accommodate all pets!\n"
    result += "Accommodated pets:\n"
    for pet, count in pets.items():
        result += f"{pet}: {count}\n"
    return result


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
print()
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
print()
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
