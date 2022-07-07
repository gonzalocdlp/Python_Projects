MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0,
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
drink_list=[]
for drinks in MENU:
    drink_list.append(drinks)

def choose(choice):
    cost=MENU[choice]['cost']
    watercost=MENU[choice]['ingredients']['water']
    milkcost=MENU[choice]['ingredients']['milk']
    coffeecost=MENU[choice]['ingredients']['coffee']
    return cost, watercost, milkcost, coffeecost

totalwater=resources['water']
totalcoffee=resources['coffee']
totalmilk=resources['milk']
continue_game="y"
while continue_game=="y":
    choice=input(f"What would you like? {drink_list} or 'report' to check levels:").lower()
    if choice=='report':
        print(f'Water levels are {totalwater}\nCoffee levels are {totalcoffee}\nMilk levels are {totalmilk}')
    elif choice=='off':
        continue_game='n'
    else:
        cost, watercost, milkcost, coffeecost =choose(choice)
        quarters=int(input('how many quarters'))*0.25
        dimes=int(input('how many dimes'))*0.10
        knickels=int(input('how many knickels'))*0.05
        moneyput= quarters+dimes+knickels
        if cost<=moneyput:
            if watercost>totalwater:
                print('Machine needs more water. Money refunded.')
            elif coffeecost>totalcoffee:
                print('Machine needs more coffee. Money refunded.')
                
            elif milkcost>totalmilk:
                print('Machine needs more milk. Money refunded.')
            else:
                change=moneyput-cost
                print(f'your change is {change} here is your {choice}')
                totalmilk+=-milkcost
                totalmilk+=-coffeecost
                totalwater+=-watercost
        else:
            print('Not enough money. Money refunded')