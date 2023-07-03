# Coffee Machine (OOP)

This repository contains a Python script that simulates a coffee machine using Object-Oriented Programming (OOP) concepts. The script allows users to select different coffee drinks, insert coins, and receive their desired coffee.

## Application Description

The coffee machine script consists of the following classes:

### CoffeeMaker Class
File: `coffee_maker.py`

This class models the coffee machine itself. It manages the available resources (water, milk, and coffee) and provides methods to check resource sufficiency, make coffee, and print reports.

### MoneyMachine Class
File: `money_machine.py`

This class models the money handling functionality of the coffee machine. It manages the money received, calculates change, and keeps track of the machine's profit. The class provides methods to process coins, make payments, and print profit reports.

### MenuItem Class
File: `menu_item.py`

This class represents each individual coffee drink available in the menu. It holds the name, cost, and required ingredients of each drink.

### Menu Class
File: `menu.py`

This class models the menu of the coffee machine. It contains a list of `MenuItem` objects and provides methods to retrieve available drink names and find drinks by name.

### Main Script
File: `main.py`

This script creates instances of the `CoffeeMaker`, `MoneyMachine`, and `Menu` classes, and implements the main functionality of the coffee machine. It allows users to choose drinks, handles coin insertion, checks resource sufficiency, processes payments, and makes coffee.

## Dependencies

This application has no external dependencies. It uses only the Python standard library.

## Disclaimer

This application is for educational purposes and demonstrates the implementation of a coffee machine using OOP concepts. Please use it responsibly and respect the license terms.

## Contributing

If you have any improvements or suggestions for this application, feel free to contribute by creating a pull request. Your contributions are greatly appreciated!
