# Pong Game
This is a classic Pong game implemented using Python's turtle module. The game features two paddles that the players control to hit the ball and score points. The goal is to prevent the ball from crossing the player's side while trying to make the ball pass the opponent's paddle.

## Game Features:
- Control the paddles using the arrow keys for player 1 and 'W' and 'S' keys for player 2.
- Bounce the ball off the paddles and prevent it from crossing your side.
- Score points whenever the ball passes the opponent's paddle.
- The game displays the current score for each player.
- The game ends when one player reaches a certain score threshold.
## Project Structure:
- main.py: The main file to run the game. It sets up the game window, creates the game objects, handles user input, and runs the game loop.
- paddle.py: Contains the Paddle class representing the player's paddles.
- ball.py: Defines the Ball class representing the game ball. It handles the ball's movement and bouncing behavior.
- score.py: Contains the ScoreBoard class for managing and displaying the players' scores.
- dash.py: Defines the DashedDot class for drawing the dashed line in the middle of the screen.
## Dependencies:
The game requires the Python programming language and the turtle module, which is included in the Python standard library. No additional dependencies or installations are needed.

# How to Run:
To play the game, execute the main.py file using Python. The game window will open, and two players can take turns controlling their paddles to play Pong. The game ends when one player reaches the score threshold.

