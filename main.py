from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker
menu = Menu()

coffee_on = True
while coffee_on:
    options = menu.get_items
    drink_choice = input(f'What would you like to drink? ${options}: ').lower()
    
    if drink_choice == 'off':
        print('Powering down in :')
        time.sleep(1.5)
        print('3')
        time.sleep(1.5)
        print('2')
        time.sleep(1.5)
        print(1)
        time.sleep(1)
        print('Good Bye')
        coffee_on = False
    elif drink_choice == 'report':
        coffee_maker.report
        money_machine.report
    else:
        drink = menu.find_drink(drink_choice)
        if coffee_maker.is_resource_sufficient(drink):
            print('Insert Coins')
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        