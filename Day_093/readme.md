# Chrome Dinosaur Game Bot

This repository contains a Python script that automates the Chrome Dinosaur Game. The script uses the PyAutoGUI library to control the game and make the dinosaur jump over obstacles.

## Application Description

The Chrome Dinosaur Game Bot script consists of the following components:

### Main Script
File: `main.py`

This script implements the main functionality of the bot. It creates an instance of the `Dinosaur` class, which represents the dinosaur character in the game. The script continuously checks for obstacles ahead using the `sees_obstacle_ahead()` method. If an obstacle is detected, the script makes the dinosaur jump using the `jump()` method.

The `Dinosaur` class has the following methods:

- `jump()`: Simulates a jump by pressing and releasing the 'up' key using the PyAutoGUI library.
- `sees_obstacle_ahead() -> bool`: Checks if there is an obstacle ahead of the dinosaur. It analyzes the pixel color at a specific location on the screen to determine the presence of an obstacle.


Please note that the script interacts with your screen using PyAutoGUI, so make sure the Chrome browser window is visible and in the foreground while running the script.

Feel free to customize the script to adjust the jump timing or add additional functionality to enhance the bot's performance.

## Dependencies

This application depends on the following external library:

- PyAutoGUI: Used to control the game and simulate key presses. Install it using `pip install pyautogui`.

## Disclaimer

This application is for educational purposes and automates the Chrome Dinosaur Game. Please use it responsibly and respect the game's terms of service.

## Contributing

If you have any improvements or suggestions for this application, feel free to contribute by creating a pull request. Your contributions are greatly appreciated!
