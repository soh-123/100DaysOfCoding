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

def intro():
# This function introduces the rules of the game Tic Tac Toe
    art = """        88                                                              
    ,d    ""              ,d                            ,d                
    88                    88                            88                
    MM88MMM 88  ,adPPYba, MM88MMM ,adPPYYba,  ,adPPYba, MM88MMM ,adPPYba,   
    88    88 a8"     ""   88    ""     `Y8 a8"     ""   88   a8"     "8a  
    88    88 8b           88    ,adPPPPP88 8b           88   8b       d8  
    88,   88 "8a,   ,aa   88,   88,    ,88 "8a,   ,aa   88,  "8a,   ,a8"  
    "Y888 88  `"Ybbd8"'   "Y888 `"8bbdP"Y8  `"Ybbd8"'   "Y888 `"YbbdP"'   
                                                                            
                                                                                 
            
    """
    print(art)
    print("Hello! Welcome to Pam's Tic Tac Toe game!")
    print("\n")
    print("Rules: Player 1 and player 2, represented by X and O, take turns "
          "marking the spaces in a 3*3 grid. The player who succeeds in placing "
          "three of their marks in a horizontal, vertical, or diagonal row wins.")
    print("\n")
    input("Press enter to continue.")
    print("\n")

def create_board(spots):
    """Create a board"""
    print("Here is the playboard: ")   
    print(f"|{spots[1]}|{spots[2]}|{spots[3]}|\n|{spots[4]}|{spots[5]}|{spots[6]}|\n|{spots[7]}|{spots[8]}|{spots[9]}|") 

def check_turn(turn):
    if turn %2 == 0:
        return 'O'
    else:
        return 'X'
    
def check_for_win(spots):
    if (spots[1] == spots[2] == spots[3])\
    or (spots[4] == spots[5] == spots[6])\
    or (spots[7] == spots[8] == spots[9]):
        return True
    elif (spots[1] == spots[4] == spots[7])\
    or (spots[2] == spots[5] == spots[8])\
    or (spots[3] == spots[6] == spots[9]):
        return True
    elif (spots[1] == spots[5] == spots[9])\
    or (spots[3] == spots[5] == spots[7]):
        return True
    else:
        return False
    

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