from ng_art import logo
import random

#set global constant
EASY_LEVER_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """Compares the guessed number and the answer and returns the remaining turns"""
    if guess > answer:
        print("Too high")
        return turns-1
    elif guess < answer:
        print("Too low")
        return turns-1
    elif guess == answer:
        print(f"You got it, the answer is {guess}")

def difficulty():
    """Check game level that user choosed"""
    hardness = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if hardness == "easy":
        return EASY_LEVER_TURNS
    else:
        return HARD_LEVEL_TURNS

def game(): 
    """The main function that runs the game"""      
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    #generate random number
    answer = random.randint(1,100)

    print(answer) 
    turns = difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer,turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return 0
        elif guess != answer:
            print("Guess again!")

game()
