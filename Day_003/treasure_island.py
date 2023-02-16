#Write treasure island game to lead the user to the treasure

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

start = input("Let\'s get started! write y or n to continue\n").lower()
if start == "y":
  print("Your ship has just landed on the mystery island, there are two different ways\n One of your crew suggested going left and another suggested the right way.\n ")
  choice1 = input("Which way do you take? Write Right or Left to continue ..\n").lower()
  if choice1 == "left":
    print("That way leading to a beatiful lake, if you swim you will cross the lake faster but since it's a mysterious island you could keep going around the lake to get to the other side\n")
    choice2 = input("Which way will you take? write Swim or Wait to continue .. \n").lower()
    if choice2 == "wait":
      print("Smart choice, now you walk longer but more safely.\n You have found the treasure, but before you approach a wise man comes to tell you that only one has the treasure and the rest will cause your death\n")
      choice3 = input("Which box will you open? Write red, blue, or yellow to continue ..\n").lower()
      if choice3 == "yellow":
        print("Congratulation! you found the treasure\n")
        print('''
                        '
               '                 '
       '         '      '      '        '
          '        \    '    /       '
              ' .   .-"```"-.  . '
                    \`-._.-`/
         - -  =      \\ | //      =  -  -
                    ' \\|// '
              . '      \|/     ' .
           .         '  `  '         .
        .          /    .    \           .
                 .      .      .''')
      elif choice3 == "red":
        print("A box full of snakes, GAME OVER!")
      elif choice3 == "blue":
        print("An empty Box, GAME OVER!")
    elif choice2 == "swim":
      print("You have been eaten by nile crocodile")
  elif choice1 == "right":
    print("The right way is full of traps killed your crew, GAME OVER!")
elif start == "n":
  print("See you next time! bye bye.")
