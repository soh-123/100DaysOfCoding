# Tic Tac Toe Game

The Tic Tac Toe game is a classic two-player game implemented using a Python script. It provides a command-line interface where players can take turns marking spots on a 3x3 board until one of them wins or the game ends in a draw.

## Features:

- Board Visualization: The game starts by displaying an empty board with numbered spots. Players choose a number representing the spot they want to mark with their respective symbols ('X' or 'O'). The board is updated after each turn to reflect the current state of the game.

- Turn-Based Gameplay: The game alternates turns between Player 1 and Player 2. Each player enters a number between 1 and 9 to select a spot on the board. The script validates the input and prevents players from selecting an already marked spot or entering an invalid choice.

- Win Detection: After each turn, the script checks for a winning condition. If any player successfully forms a horizontal, vertical, or diagonal line with their symbols, they are declared the winner, and the game ends.

- Draw Detection: If all spots on the board are filled, and no player has achieved a winning condition, the game ends in a draw. The script detects this scenario and displays a "Draw!" message.

- Quitting the Game: At any point during the game, a player can press 'q' to quit, and the game will end immediately.