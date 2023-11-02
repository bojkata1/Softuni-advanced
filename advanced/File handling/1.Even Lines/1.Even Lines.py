with open("text.txt", "r") as file:
    for row, line in enumerate(file.readlines()):
        if row % 2 == 0:
            for char in "-,.!?":
                line = line.replace(char, "@")
            print(" ".join(reversed(line.split())))
