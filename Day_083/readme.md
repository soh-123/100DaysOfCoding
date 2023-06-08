# Tic Tac Toe Game

The Tic-Tac-Toe project is a classic game implemented in Python. It provides a command-line interface (CLI) for users to play the popular game of Tic-Tac-Toe against each other.

## Game Rules

Tic-Tac-Toe is a two-player game played on a 3x3 grid. The players take turns marking spaces on the grid with their respective symbols (X or O). The goal is to get three of their symbols in a horizontal, vertical, or diagonal row.

## Features:

- Board Visualization: The game starts by displaying an empty board with numbered spots. Players choose a number representing the spot they want to mark with their respective symbols ('X' or 'O'). The board is updated after each turn to reflect the current state of the game.

- Turn-Based Gameplay: The game alternates turns between Player 1 and Player 2. Each player enters a number between 1 and 9 to select a spot on the board. The script validates the input and prevents players from selecting an already marked spot or entering an invalid choice.

- Win Detection: After each turn, the script checks for a winning condition. If any player successfully forms a horizontal, vertical, or diagonal line with their symbols, they are declared the winner, and the game ends.

- Draw Detection: If all spots on the board are filled, and no player has achieved a winning condition, the game ends in a draw. The script detects this scenario and displays a "Draw!" message.

- Quitting the Game: At any point during the game, a player can press 'q' to quit, and the game will end immediately.
  
## Acknowledgments

The Tic-Tac-Toe project was developed as a fun exercise to practice Python programming and logic. It draws inspiration from the classic game of Tic-Tac-Toe and various online resources and tutorials.

Feel free to customize and enhance the game according to your preferences. Contributions and suggestions are always welcome!

Enjoy playing Tic-Tac-Toe with your friends using this Python implementation!