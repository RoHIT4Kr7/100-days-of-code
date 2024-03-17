MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
import os

def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def process_coffee(coffee_type, cost):
    global resources
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total_value = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    if resources['water']>MENU[coffee_type]['ingredients'].get('water', 0) and resources['coffee']>MENU[coffee_type]['ingredients'].get('coffee', 0) and resources['milk']>MENU[coffee_type]['ingredients'].get('milk', 0):
        if total_value == cost:
            print(f"Here is your {coffee_type} ☕ ENJOY!!")
            resources['money'] += cost
            resources['coffee'] -= MENU[coffee_type]['ingredients'].get('coffee', 0)
            resources['water'] -= MENU[coffee_type]['ingredients'].get('water', 0)
            resources['milk'] -= MENU[coffee_type]['ingredients'].get('milk', 0)
        elif total_value > cost:
            print(f"Please collect your change: ${total_value - cost}")
            print(f"Here is your {coffee_type} ☕ ENJOY!!")
            resources['money'] += cost
            resources['coffee'] -= MENU[coffee_type]['ingredients'].get('coffee', 0)
            resources['water'] -= MENU[coffee_type]['ingredients'].get('water', 0)
            resources['milk'] -= MENU[coffee_type]['ingredients'].get('milk', 0)
        else:
            print("SORRY THAT'S NOT ENOUGH MONEY. MONEY REFUNDED")
    elif resources['water']<MENU[coffee_type]['ingredients'].get('water', 0):
        print(f"SORRY WATER IS NOT THERE,{coffee_type} NOT POSSIBLE, COLLECT YOUR CHANGE")
    elif resources['coffee']>MENU[coffee_type]['ingredients'].get('coffee',0):
        print(f"SORRY COFFEE IS NOT THERE,{coffee_type} NOT POSSIBLE, COLLECT YOUR CHANGE")
    elif resources['milk']>MENU[coffee_type]['ingredients'].get('milk',0):
        print(f"SORRY MILK IS NOT THERE,{coffee_type} NOT POSSIBLE, COLLECT YOUR CHANGE")

def coffee_machine():
    global MENU, resources
    while True:
        ask_user = input('What would you like? (espresso/latte/cappuccino): ').lower()
        if ask_user == "off":
            print("Coffee machine is switched off.")
            break
        elif ask_user in MENU:
            print("PLEASE INSERT COINS🪙")
            process_coffee(ask_user, MENU[ask_user]['cost'])
        elif ask_user == "report":
            print(resources)
        else:
            print("Invalid input.")

coffee_machine()
