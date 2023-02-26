# write a program that tests the compatibility between two people.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower = name1.lower()
name2_lower = name2.lower()
both = name1_lower + name2_lower
true = both.count("t") + both.count("r") + both.count("u") + both.count("e")

love = both.count("l") + both.count("o") + both.count("v") + both.count("e")

score = int(str(true) + str(love))
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score < 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
