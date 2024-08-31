def get_action_input():
    return input("What would you like to do?\n")

def play():
    arr_inventory = ['Dagger', 'Gold(5)', 'Crusty Bread', 'Great Axe']
    user_still_active = True
    print("Welcome to Greed Island -_____-")

    while user_still_active:
        user_action = get_action_input()

        if user_action in ['n', 'N', 'north', 'North', '^']:
            print("You are going North!")
        elif user_action in ['e', 'E', 'east', 'East', '>']:
            print("You are going East!")
        elif user_action in ['s', 'S', 'south', 'South', 'v']:
            print("You are going South!")
        elif user_action in ['w', 'W', 'west', 'West', '<']:
            print("You are going West!")
        elif user_action in ['i', 'I', 'inventory', 'Inventory']:
            print("You have access to the following items in your inventory:\n")

            for i, item in enumerate(arr_inventory, 1):
                print(f"{i}. {item}")
        elif user_action in ['q', 'Q', 'quit', 'Quit']:
            print("It's been a pleasure; travel safe...")
            user_still_active = False
        else:
            print("You have chosen wrong; try again...")

play()
