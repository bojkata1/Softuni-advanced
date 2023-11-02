import os


while True:
    command = input()
    if command == "End":
        break
    command, filename, *args = command.split("-")

    if command == "Create":
         open(filename, "w").close()

    elif command == "Add":
        with open(filename, "a") as file:
            file.write(f"{args[0]}\n")

    elif command == "Replace":
        old_string, new_string = args
        try:
            with open(filename, "r") as file:
                content = file.read()
        except FileNotFoundError:
            print("An error occurred")
        else:
            with open(filename, "w") as file:
                file.write(content.replace(old_string, new_string))
    elif command == "Delete":
        try:
            os.remove(filename)
        except FileNotFoundError:
            print("An error occurred")

