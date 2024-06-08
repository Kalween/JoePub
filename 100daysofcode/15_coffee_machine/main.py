machine_on = True
QUARTERS = 0.25 
DIMES = 0.10 
NICKLES = 0.05 
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

# def inventory(i, q, orderup):
#     if resources[i][q] <= 
def input_coins(orderup):
    amount = 0
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? ")) 
    amount += quarters * QUARTERS
    amount += dimes * DIMES
    amount += nickles * NICKLES
    amount += pennies * PENNIES
    cost = MENU[orderup]['cost']
    if amount < cost:
        print("Not enough money")
        return
    else:
        cashback = amount - MENU[orderup]['cost']
        print(f"Awesome, and here is your return ${round(cashback,2)}")

def choices(orderup):
    for i , q in MENU[orderup]['ingredients'].items():
        # print(i, q)
        # print(resources[i])
        if q > resources[i]:
            print(f"Not enough {i}. Please come back later")
            return
        else:
            resources[i] = resources[i] - q
    input_coins(orderup)

while machine_on == True:
    orderup = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if orderup == 'off':
        machine_on = False
    elif orderup == 'report':
        print(resources)
    else:
        choices(orderup)



