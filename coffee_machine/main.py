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


def print_report():
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${resources['money']}\n")


def make_coffee(coffee_option):
    if coffee_option == "espresso":
        resources['water'] -= MENU['espresso']['ingredients']['water']
        resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
    elif coffee_option == "latte":
        resources['water'] -= MENU['latte']['ingredients']['water']
        resources['milk'] -= MENU['latte']['ingredients']['milk']
        resources['coffee'] -= MENU['latte']['ingredients']['coffee']
    elif coffee_option == "capuccino":
        resources['water'] -= MENU['capuccino']['ingredients']['water']
        resources['milk'] -= MENU['capuccino']['ingredients']['milk']
        resources['coffee'] -= MENU['capuccino']['ingredients']['coffee']


# TODO 4 - Check if the resources are sufficient to make a drink
def check_resources(coffee_option):
    if coffee_option == "espresso":
        if resources['water'] < 50:
            print("Sorry there is not enough water!")
        elif resources['coffee'] < 18:
            print("Sorry there is not enough coffee!")
        else:
            payment(coffee_option)
    elif coffee_option == "latte":
        if resources['water'] < 200:
            print("Sorry there is not enough water!")
        elif resources['milk'] < 150:
            print("Sorry there is not enough milk!")
        elif resources['coffee'] < 24:
            print("Sorry there is not enough coffee!")
        else:
            payment(coffee_option)
    elif coffee_option == "capuccino":
        if resources['water'] < 250:
            print("Sorry there is not enough water!")
        elif resources['milk'] < 100:
            print("Sorry there is not enough milk!")
        elif resources['coffee'] < 24:
            print("Sorry there is not enough coffee!")
        else:
            payment(coffee_option)


# TODO 5 - If there are sufficient resources, ask for the coins and calculate the value
def payment(coffee_option):
    print("Please insert coins.")
    quarters = int(input("How many quarters?")) * 0.25
    dimes = int(input("How many dimes?")) * 0.10
    nickels = int(input("How many nickels?")) * 0.05
    pennies = int(input("How many pennies?")) * 0.01
    total = quarters + dimes + nickels + pennies

    # TODO 6 - Check if transaction was successful
    if coffee_option == 'espresso':
        if total >= MENU['espresso']['cost']:
            print(f"Here is ${total - MENU['espresso']['cost']} in change.")
            print(f"Here is your espresso ☕. Enjoy!\n")
            make_coffee(coffee_option)
        else:
            print(f"Sorry! That's not enough money.\nMoney refunded!\n")
    elif coffee_option == 'latte':
        if total >= MENU['latte']['cost']:
            print(f"Here is ${total - MENU['latte']['cost']} in change.")
            print(f"Here is your latte ☕. Enjoy!\n")
            make_coffee(coffee_option)
        else:
            print(f"Sorry! That's not enough money.\nMoney refunded!\n")
    elif coffee_option == 'capuccino':
        if total >= MENU['capuccino']['cost']:
            print(f"Here is ${total - MENU['capuccino']['cost']} in change.")
            print(f"Here is your capuccino ☕. Enjoy!\n")
            make_coffee(coffee_option)
        else:
            print(f"Sorry! That's not enough money.\nMoney refunded!\n")


user_request = ''
# TODO 2 - Turn off the coffee machine when entering "off" at the prompt
while user_request != "off":
    # TODO 1 - Ask the user what he would like (espresso/latte/capuccino)
    user_request = input("What would you like? (espresso/latte/capuccino): ").lower()

    # TODO 3 - Print a report with the remaining resources on the machine
    if user_request == "report":
        print_report()
    else:
        check_resources(user_request)