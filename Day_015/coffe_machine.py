from cofee_machine_art import*
from coffe_machine_data import*

def coins_calculator():
    """takes coin numbers and calculate the total coins that user entered"""
    quarter = int(input("how many quarters?: ")) * 0.25
    dime = int(input("how many dimes?: ")) * 0.10
    nickle = int(input("how many nickles?: ")) * 0.05
    penny = int(input("how many pennies?: ")) * 0.01

    total_input = quarter + dime + nickle + penny
    return total_input

def check_resources(order_ingredient):
    """Check on each resource and returns true if there's enough and false if there isn't"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.”")
            return False
        return True
    
def make_coffee(order_ingredient):
    """Deduct the required ingredients from resources"""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]

print(logo)

profit = 0
is_on = True
while is_on:
    #Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    USER_CHOICE = input("What would you like? (espresso/latte/cappuccino):")
    if USER_CHOICE == "off":
        is_on = False
    
    elif USER_CHOICE == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else: 
        drink = MENU[USER_CHOICE]["ingredients"]
        price = MENU[USER_CHOICE]["cost"]
        if check_resources(drink):
        
            # ask the user to insert the coins: quarter, dimes,  nickel, pennies 
            print(f"Total price: {price}, Please insert coins.")
            changes = round(coins_calculator() - price, 2)
            if changes > 0:
                profit += price
                print(f"Here is ${changes} in change.")
                make_coffee(drink)
                print(f"Here is your {USER_CHOICE} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
                is_on = False

