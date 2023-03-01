from coffee_maker import*

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

#TODO: print report
coffee_maker.report()
money_machine.report()

#TODO: Check resources suffecient
while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? ({option})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        #TODO: process coin
        #TODO: chaeck transaction succesful
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          #TODO: Make coffee
          coffee_maker.make_coffee(drink)



