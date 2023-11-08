import os

# I've added test files in the root directory and in a folder "Test" to make testing the code easier

directory = input()
file_types = {}
for element in os.listdir(directory):
    f = os.path.join(directory, element)
    if os.path.isfile(f):
        extension = f".{element.split('.')[-1]}"
        if extension not in file_types:
            file_types[extension] = []
        file_types[extension].append(element)
    else:
        for el in os.listdir(f):
            filename = os.path.join(f, el)
            if os.path.isfile(filename):
                extension = f".{el.split('.')[-1]}"
                if extension not in file_types:
                    file_types[extension] = []
                file_types[extension].append(el)

with open("report.txt", "w") as f:
    for k, v in sorted(file_types.items()):
        f.write(k + "\n")
        for name in sorted(v):
            f.write(f"- - - {name}\n")
