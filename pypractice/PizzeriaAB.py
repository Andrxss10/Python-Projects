#TITLE
print("---------|Pizzeria - AB|----------")

#DESCRIPTION
print("Welcome to Pizzeria AB the best pizzeria around the world")

#VARIABLES
pizzas = {
    1:{"name": "Pepperoni", "price": 13},
    2:{"name": "Extra Cheese", "price": 11},
    3:{"name": "Vegetarian", "price": 18}
}

toppings = {
    1:{"name": "Pepperoni", "price": 2},
    2:{"name": "Cheese", "price": 1.5},
    3:{"name": "Tomato", "price": 1},
    4:{"name": "Onion", "price": 0.8},
    5:{"name": "Meat", "price": 2.5},
}

current_order = {}
final_value = 0

while True:
    try:
        #USER BALANCE VARIABLE
        user_balance = float(input("Please, enter your balance: "))
        if user_balance:
            break
    except ValueError:
        print("Enter a numeric balance")

while True:
    print("-|-----MENU-----|-")
    for num, info in pizzas.items():
        print(f"-{num}. {info['name']} ${info['price']}")
    print("-4. EXIT")

    while True:
        try:
            pizza_option = int(input("Select your favorite pizza in menu(only numbers)"))
            if pizza_option:
                if pizza_option in [1,2,3,4]:
                    break
                else:
                    print("Enter a valid numeric option in range 1-4")
        except ValueError:
            print("Enter a valid numeric option")

    if pizza_option == 4:
        print("See you later !!")
        break

    current_order = {
        "pizza": pizzas[pizza_option]["name"],
        "initial_price": pizzas[pizza_option]["price"],
        "toppings": [],
        "total": pizzas[pizza_option]["price"]
        }

    print("Now, add the toppings that you preffer: ")
    print("-|-----TOPPINGS-----|-")
    for num, topping in toppings.items():
        print(f"-{num}. {topping['name']} ${topping['price']}")
    print("-0. Finish order and pay")

    while True:
        try:
            toppings_option = int(input("Now, add the toppings that you prefer(if you don't want enter 0):"))

            if toppings_option == 0:
                break
            
            if toppings_option:
                if toppings_option in [1,2,3,4,5]:
                    current_order["toppings"].append(toppings[toppings_option]["name"])
                    current_order["total"] += toppings[toppings_option]["price"]
                    print(f"You just added the following toppings: {toppings[toppings_option]['name']}")
                else:
                    print("Enter a valid numeric option in range 1-6")
                    
        except ValueError:
            print("Enter a valid numeric option")

    print(f"Your balance right now is: {user_balance}")
    print("Your order right now is: ")
    print(f"- Pizza: {current_order['pizza']}")
    print(f"- Toppings: {current_order['toppings']}")
    print(f"- Total: {current_order['total']}")

    if current_order["total"] <= user_balance:
        final_value += current_order["total"]
        print(f"Total payment: {final_value}")
        print("Completing the purchase and deducting from the user balance...")
        user_balance -= current_order["total"]
        print(f"User Balance after purchase: {user_balance}")
        break
    else:
        print("Your balance is insufficient, please try ordering again")
        break
print(f"Feliz navidad {user_balance}")







        
    
