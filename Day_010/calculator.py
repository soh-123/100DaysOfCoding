import os
from calculator_art import logo


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": sub, "*": multiply, "/": divide}


def calculator():
    print(logo)
    first_number = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    game_over = False
    while not game_over:
        op = input("Pick an operation from the line above: ")
        second_number = float(input("What'\s the next number? "))
        calculation_function = operations[op]
        answer = calculation_function(first_number, second_number)

        print(f"{first_number} {op} {second_number} = {answer}")

        quit_calculator = input(
            f"Type y to continue with {answer}, type n to restart, or e to exit"
        )
        if quit_calculator == "y":
            first_number = answer
        elif quit_calculator == "n":
            os.system("clear")
            calculator()
        else:
            print("Byeee")
            game_over = True


calculator()
