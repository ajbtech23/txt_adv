def get_shopping_item():
    return input("What would you like to add to your shopping list?\n")

def play():
    print("Welcome to the Le Wagon store; it's a pleasure to have you :D")

    is_user_still_shopping = True
    user_shopping_cart = []

    while is_user_still_shopping:
        user_action = get_shopping_item()

        if user_action in ['q', 'Q', 'quit', 'Quit']:
            print("\nIt\'s been a pleasure making your acquitance XD\n")
            is_user_still_shopping = False
        else:
            user_shopping_cart.append(user_action)


    for good in user_shopping_cart:
        print(f"You have chosen to buy: {good}")

play()
