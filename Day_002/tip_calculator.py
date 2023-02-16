#Create a tip calculator 
print("welcome to the tip calculator!")
total = float(input("what was the total bill? "))
people = int(input("how many person to split on? "))
tip = int(input("please enter the tip percent from the following:\n 0 - 5 - 10 - 12 - 15\n"))
per_person = total/people
tip_decimal = (tip/100) * per_person
final = round(tip_decimal + per_person,2)
final = "{:.2f}".format(tip_decimal + per_person)
print(f"each one of the {people} will pay {round(final, 2)}")