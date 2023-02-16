# Write a program that works out whether if a given year is a leap year. 
year = int(input("Which year do you want to check? "))
if year%4 == 0:
  print("Leap year.")
elif year%100 == 0:
  print("Leap year.")
elif year%400 == 0:
  print("Leap year.")
else:
  print("Not leap year.")

"""
another solution
if year%4 == 0:
  if year%100 == 0:
    if year%400 == 0:
      print("leap year")
    else:
      print("not leap year")
  else:
    print("leap year")  
else:
  print("Not leap year.")
"""
