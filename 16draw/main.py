from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
moneymachine=MoneyMachine()
coffeemaker=CoffeeMaker()
continue_game="y"
while continue_game=="y":
    choice=input(f"pick {menu.get_items()}").lower()
    if choice=="off":
        continue_game="n"
    elif choice=="report":
        coffeemaker.report()
        moneymachine.report()
    else:
        drink=menu.find_drink(choice)
        resources=coffeemaker.is_resource_sufficient(drink)
        price=drink.cost
        payment=moneymachine.make_payment(price)
        if payment==True:
            if resources==True :
                coffeemaker.make_coffee(drink)
            else:
                print('not enough resources')
    



