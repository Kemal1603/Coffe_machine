menu = {
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
    "money": 0,
}


def user_request_handler(beverages_menu, resources_left, user_request):
    for ingredients in beverages_menu[user_request]['ingredients']:
        resources_left[ingredients] -= beverages_menu[user_request]['ingredients'][ingredients]
        if resources_left[ingredients] <= 0:
            return False
    resources_left['money'] += beverages_menu[user_request]['cost']
    return True


def price_handler():
    quarter = int(input('how many quarters?: ')) * 25
    dimes = int(input('how many dimes?: ')) * 10
    nickles = int(input('how many nickles?: ')) * 5
    pennies = int(input('how many pennies?: ')) * 1
    return (quarter + dimes + nickles + pennies) / 100


def resources_in_tank(resources_list):
    empty = 3
    for each_resource in resources_list:
        if each_resource == 'money':
            continue
        elif resources_list[each_resource] == 0:
            empty -= 1
    if empty == 3:
        return True
    else:
        return False


while resources_in_tank(resources):

    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == 'report':
        for key in resources:
            print(f"{key}: {resources[key]}")
    else:
        if user_request_handler(menu, resources, user_input):
            print('Please insert coins')
            surrender = price_handler() - menu[user_input]['cost']
            if surrender < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is $ {round(surrender, 2)} in change.\nHere is your {user_input}. Enjoy!")
        else:
            print('Unfortunately there is no enough resources in a machine')


