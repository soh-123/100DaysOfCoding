# write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
number_item = len(names)
random_item = random.randint(0, number_item-1)
person = names[random_item]
print(f"{person} is going to buy the meal today!")