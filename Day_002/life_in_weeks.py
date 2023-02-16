# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
age = input("What is your current age? ")
a = 90-int(age)
month = a*12
week = a*52
day = a*365
print(f"You have {day} days, {week} weeks, and {month} months left.")


