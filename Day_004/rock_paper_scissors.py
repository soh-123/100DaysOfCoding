import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = [rock, paper, scissors]
user_choice = int(input("What do you choose? type 0 for rock, 1 for paper and 2 for scissors.\n"))
print(game_list[user_choice])

computer = random.randint(0,2)
print(game_list[computer])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer == 2:
  print("You win!")
elif computer == 0 and user_choice == 2:
  print("You lose")
elif computer > user_choice:
  print("You lose")
elif user_choice > computer:
  print("You win!")
elif computer == user_choice:
  print("It's a draw")