# Coffee Machine

This repository contains a Python script that simulates a coffee machine. The script allows users to choose from a variety of coffee drinks, insert coins for payment, and receive their desired coffee. 

## Application Description

The coffee machine script consists of the following components:

### `cofee_machine_art` Module
File: `cofee_machine_art.py`

This module contains ASCII art used for displaying the coffee machine logo.

### `coffe_machine_data` Module
File: `coffe_machine_data.py`

This module contains the menu and resources data used by the coffee machine script.

### Main Script
File: `main.py`

This script implements the main functionality of the coffee machine. It prompts the user to choose a coffee drink and handles the payment process. The script also checks the availability of resources, calculates change, deducts ingredients from resources, and dispenses the chosen coffee.

The script utilizes the following functions:

- `coins_calculator()`: Takes the number of coins from the user and calculates the total amount entered.
- `check_resources(order_ingredient)`: Checks if there are sufficient resources to make the selected coffee drink.
- `make_coffee(order_ingredient)`: Deducts the required ingredients from the available resources.
- `print_report()`: Prints a report of the current resource levels and profit.

The script uses the `MENU` dictionary to store the available coffee drinks along with their ingredients and costs. The `resources` dictionary holds the initial resource levels.

## Dependencies

This application has no external dependencies. It uses only the Python standard library.

## Disclaimer

This application is for educational purposes and simulates a coffee machine. Please use it responsibly and respect the license terms.

## Contributing

If you have any improvements or suggestions for this application, feel free to contribute by creating a pull request. Your contributions are greatly appreciated!