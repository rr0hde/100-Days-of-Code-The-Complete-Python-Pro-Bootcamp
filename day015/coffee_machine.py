def report(resource):
    print(f"Water: {resource['water']}ml")
    print(f"Milk: {resource['milk']}ml")
    print(f"Coffee: {resource['coffee']}g")
    print(f"Money: ${resource['money']:.2f}")


def check_resources(coffee, resource, menu):
    for i in resource:
        if resource[i] < menu[coffee]['ingredients'][i]:
            return print(f"Sorry, there is not enough {i}")
        else:
            return True


def make_coffee(coffee, resource, menu):
    resource['water'] -= menu[coffee]['ingredients']['water']
    resource['coffee'] -= menu[coffee]['ingredients']['coffee']
    if 'milk' in menu[coffee]['ingredients']:
        resource['milk'] -= menu[coffee]['ingredients']['milk']
    return resource


def process_coins(q_coin, d_coin, n_coin, p_coin, coins, coffee, menu, resource):
    total = q_coin * coins['quarter'] + d_coin * coins['dime'] + n_coin * coins['nickel'] + p_coin * coins['penny']
    if total < menu[coffee]['cost']:
        return False
    else:
        resource['money'] += menu[coffee]['cost']
        total -= menu[coffee]['cost']
        return '{0:.2f}'.format(total)


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

make_more = True

while make_more:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input != "report" and user_input != "off":
        if check_resources(user_input, resources, MENU):
            print("Please insert coins.")
            q_coin = int(input("How many quarters?: "))
            d_coin = int(input("How many dimes?: "))
            n_coin = int(input("How many nickels?: "))
            p_coin = int(input("How many pennies?: "))
            total = process_coins(q_coin, d_coin, n_coin, p_coin, coins, user_input, MENU, resources)
            if not total:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                print(f"Here is ${total} in change.")
                make_coffee(user_input, resources, MENU)
                print(f"Here is your {user_input} ☕ Enjoy!")
    elif user_input == "report":
        report(resources)
    elif user_input == "off":
        make_more = False
