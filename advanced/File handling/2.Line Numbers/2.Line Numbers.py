from string import punctuation

with open("text.txt", "r") as input_file, open("output.txt", "w") as output_file:
    for row, line in enumerate(input_file, start=1):
        char_counter = 0
        punctuation_counter = 0
        for char in line:
            if char.isalpha():
                char_counter += 1
            elif char in punctuation:
                punctuation_counter += 1
        output_file.write(f"Line {row}: {line.strip()} ({char_counter})({punctuation_counter})\n")
