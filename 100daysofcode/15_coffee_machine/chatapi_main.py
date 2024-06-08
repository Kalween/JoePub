### Comments on my code with refactor:
"""
Your code looks pretty good! It's well-organized and easy to follow. Here are a few suggestions for refactoring to improve readability and maintainability:

Constants Naming: Use uppercase with underscores for constant variables like QUARTERS, DIMES, NICKELS, and PENNIES for consistency.
Function for Coin Input: You could create a separate function to handle coin input and return the total amount. This can help clean up the choices function and make it more focused on its task.
Function for Checking Resources: Consider creating a function to check if there are enough resources for the chosen drink. This function can be reused whenever you need to check resources for any drink.
Use f-strings: Utilize f-strings for string formatting, it makes the code more readable and concise.
"""

MACHINE_ON = True
QUARTERS = 0.25
DIMES = 0.10
NICKELS = 0.05
PENNIES = 0.01

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
}

def input_coins(cost):
    amount = 0
    amount += float(input("How many quarters? ")) * QUARTERS
    amount += float(input("How many dimes? ")) * DIMES
    amount += float(input("How many nickels? ")) * NICKELS
    amount += float(input("How many pennies? ")) * PENNIES
    
    if amount < cost:
        print("Not enough money")
        return False
    else:
        cashback = amount - cost
        print(f"Awesome, and here is your return ${cashback:.2f}")
        return True

def check_resources(ingredients):
    for item, quantity in ingredients.items():
        if quantity > resources[item]:
            print(f"Not enough {item}. Please come back later")
            return False
    return True

def process_order(order):
    if order == 'off':
        global MACHINE_ON
        MACHINE_ON = False
    elif order == 'report':
        print(resources)
    else:
        drink = MENU.get(order)
        if drink:
            ingredients = drink['ingredients']
            cost = drink['cost']
            if check_resources(ingredients):
                if input_coins(cost):
                    for item, quantity in ingredients.items():
                        resources[item] -= quantity
                    print(f"Here is your {order}. Enjoy!")
        else:
            print("Invalid selection. Please try again.")

while MACHINE_ON:
    order_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    process_order(order_input)