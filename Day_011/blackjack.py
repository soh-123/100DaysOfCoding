from blackjack_art import *
import random
import os


def deal_cards():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Generic function to calculate the score and adjust the ace value"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) == 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "You lose, oponent had blackjack!"
    elif user_score == 0:
        return "You win with a blackjack!"
    elif user_score > 21:
        return "you went over, you lose!"
        return "You win with a blackjack!"
    elif computer_score > 21:
        return "Oponent went over, you win."
    elif user_score > computer_score:
        return "You win!"
    else:
        return "you lose!"


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(
            f"Your cards: {user_cards}, current score is {user_score} \n Computer's score: {computer_cards[0]}"
        )

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            deal_again = input(
                "Do you want to play a game of Blackjack? Type 'y' or 'n': "
            )
            if deal_again == "y":
                user_cards.append(deal_cards())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    compare(user_score, computer_score)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system("clear")
    play_game()
