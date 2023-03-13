import pandas

data = pandas.read_csv("Day_026/nato_phonetic_alphabet.csv", header=0, index_col=0, squeeze = True)
dictionary = data.to_dict()

name = input("Please enter your name: ").upper()

new_word = [dictionary[n] for n in name if n in dictionary]
print(new_word)
