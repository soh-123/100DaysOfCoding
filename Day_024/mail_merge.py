with open("Day_024/invited_names.txt") as NamesFile:
    names = NamesFile.readlines()
    print(names)

with open("Day_024/starting_letter.txt", "r") as letter:
    letter_contents = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace("[name]", stripped_name)
        with open(f"Day_024/new_letters/letter_for_{stripped_name}.txt", "w") as create_letter:
            create_letter.write(new_letter)

