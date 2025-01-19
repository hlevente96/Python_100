from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

while True:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        break
    elif choice == "report":
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)