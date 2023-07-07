# Alien Invasion Game

This is a simple Alien Invasion game implemented using Python and the Turtle graphics library. The objective of the game is to control a spaceship and shoot down the invading aliens while avoiding collisions with them. The game features a player-controlled spaceship, moving aliens, and a scoring system.

## How to Play

1. Run the `main.py` file to start the game.
2. Control the spaceship using the Left and Right arrow keys to move it horizontally.
3. Press the Spacebar to shoot bullets from the spaceship and destroy the aliens.
4. Avoid collisions with the aliens. If an alien reaches the player's spaceship, the game is over.
5. The score increases every time an alien is destroyed.
6. The game continues until an alien reaches the bottom of the screen, at which point the game over screen is displayed.

## Dependencies

The game relies on the following Python libraries:

- Turtle: Used for graphics and animations.
- Math: Used for mathematical calculations.

## Project Structure

The project is organized into the following files:

- `main.py`: The main script to run the game.
- `ship.py`: Contains the Ship class, which represents the player-controlled spaceship.
- `scoreboard.py`: Contains the Scoreboard class, responsible for managing the game score.
- `aliens.py`: Contains the Aliens class, which manages the group of invading aliens.
- `bullets.py`: Contains the Bullet class, which represents the bullets fired by the spaceship.
- `images/`: A directory containing image files used for the spaceship and aliens.

## Future Enhancements

Here are some potential enhancements that can be made to the game:

- Add sound effects and background music.
- Implement different levels with increasing difficulty.
- Include power-ups or special abilities for the player.
- Improve the graphics and animations.
- Implement a high score system.

Feel free to customize and expand upon this project as you see fit. Have fun playing and developing the game!