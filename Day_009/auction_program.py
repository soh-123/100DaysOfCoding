import os
from auction_program_art import *

print(logo)

bids = {}
game_over = False


# a function to decide the heighest bidde
def heighest_bidder(record):
    max_number = 0
    winner = ""
    for i in record:
        bid_amount = record[i]
        if bid_amount > max_number:
            max_number = bid_amount
            winner = i
    print(f"{winner} won with ${max_number} bid")


while not game_over:
    name = input("What is your name? ")
    value = int(input("How much you bid? $"))
    bids[name] = value

    continue_bidding = input("Is there another bidder? \n Write yes or no \n")
    if continue_bidding == "yes":
        os.system("clear")
    elif continue_bidding == "no":
        heighest_bidder(bids)
        game_over = True
    else:
        print("Undefined input; bye bye")
        game_over = True
