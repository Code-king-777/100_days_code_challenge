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
MENU["espresso"]["ingredients"]["milk"] = 0
water = resources["water"]
milk = resources["milk"]
coffe = resources["coffee"]
money = 0
sam = True
while sam:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        sam = False
    elif user_choice == "report":
        print(f"water: {water}ml\nmilk: {milk}ml\ncoffe: {coffe}gm\nmoney: ${money}")
    elif water < MENU[user_choice]["ingredients"]["water"]:
        print("we are running out of water sorry....")
    elif milk < MENU[user_choice]["ingredients"]["milk"]:
        print("we are running out of milk sorry....")
    elif coffe < MENU[user_choice]["ingredients"]["coffee"]:
        print("we are running out of coffee sorry....")

    else:
        quarters = float(input("please insert coins.\nhow many quarters?: "))
        dimes = float(input("how many dimes?: "))
        nickles = float(input("how many nickles?: "))
        pennies = float(input("how many pennies?: "))

        total = ((0.25*quarters)+( 0.1*dimes)+(0.05*nickles)+(0.01*pennies))
        total_money = round(total,2)
        menu_cost = MENU[user_choice]["cost"]
        if total_money <= menu_cost:
            print(f"insufficient money...refund initiated ${total_money}")
        else:
            money += menu_cost
            refund_ = total_money - menu_cost
            refund = round(refund_,2)
            water -= MENU[user_choice]["ingredients"]["water"]
            milk -= MENU[user_choice]["ingredients"]["milk"]
            coffe -= MENU[user_choice]["ingredients"]["coffee"]
            print(f"here is your ${refund} in change\nenjoy your {user_choice}...")

