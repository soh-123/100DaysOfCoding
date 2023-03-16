import pandas

data = pandas.read_csv("Day_026/nato_phonetic_alphabet.csv")
dictionary = data.to_dict()

name = input("Please enter your name: ").upper()
on = True
while on:
    try:
        new_word = [dictionary[n] for n in name]
    except KeyError:
        raise ValueError ("Sorry, only letters in the alphabet please.")
    else:
        print(new_word)
