from helpers import *
import os
import random

game_on = True
turn = 0
prev_turn = -1
complete = False
spots = {
    1:'1',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
    7:'7',
    8:'8',
    9:'9'
}
intro()
while game_on:
    os.system('cls' if os.name == 'nt' else 'clear')
    create_board(spots)
    if prev_turn == turn:
        print("invalid spot, please pick another")
    prev_turn = turn
    print(f"palyer {str((turn%2)+1)}'s turn, pick a number between (1-9) or press q to quit:")

    user_input = input()

    if str.isdigit(user_input) and int(user_input) in spots:
        if not spots[int(user_input)] in {'O', 'X'}:
            turn += 1
            spots[int(user_input)] = check_turn(turn)
        # board.replace(user_input, 'X')
    elif user_input == 'q':
        game_on = False

    if check_for_win(spots):
        game_on = False
        complete: True

if not complete:
    if check_turn(turn) == 'X':
        print("Player1 wins")
    else:
       
        print("Player2 wins")
else:
    print("Draw!")