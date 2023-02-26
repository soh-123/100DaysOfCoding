import random
from hangman_art import *
from hangman_words import *

chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
lives = 6
end_of_game = False
for _ in range(word_length):
    display += "_"

print(logo)

while not end_of_game:
    guess = input("Guess the letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")
    print(stages[lives])
