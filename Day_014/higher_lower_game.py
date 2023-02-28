from game_data import*
from higher_lower_art import *
import random
import os

def check_answer(guess, a_followers, b_followers):
    """Take user guess and follower number and returns if they got it right"""
    if a_followers > b_followers:
        if guess == "a":
            return True
        else:
            return False
    elif a_followers < b_followers:
        if guess == "a":
            return False
        else:
            return True

#display art
print(logo)
point = 0
game_over = False
choice_B = random.choice(data)

while not game_over:
    #generate a random key from dictionary for A and B
    #replace a with b to compare with the new b
    choice_A = choice_B
    choice_B = random.choice(data)

    if choice_A == choice_B:
        choice_B = random.choice(data)

    #format the account data
    print(f"Compare A: {choice_A['name']}, a {choice_A['description']}, from {choice_A['country']}.")
    print(vs)
    print(f"Against B: {choice_B['name']}, a {choice_B['description']}, from {choice_B['country']}.")

    #ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #check if user is correct
    ##get follower count of each choice
    a_follower_acount = choice_A["follower_count"]
    b_follower_acount = choice_B["follower_count"]

    is_correct = check_answer(guess, a_follower_acount, b_follower_acount)
    os.system("clear")
    if is_correct:
        point+=1
        print(f"You're right! Current score: {point}.")

    else:
        print(f"Sorry, that's wrong. Final score: {point}")
        game_over = True
        
