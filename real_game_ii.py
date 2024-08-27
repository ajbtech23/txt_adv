def get_player_cmd():
    return input("What would you like to do Sailor?\n")

def play():
    inventory = ['Dagger', 'Gold(5)', 'Crusty Bread']

    is_user_active = True
    print("Can you escape from Greed Island?! Try if you dare -_____-")

    while is_user_active:
        user_action = get_player_cmd()

        if user_action in ['n', 'N', '^']:
            print("Go North...")
        elif user_action in ['e', 'E', '>']:
            print("Go East...")
        elif user_action in ['s', 'S', 'v']:
            print("Go South...")
        elif user_action in ['w', 'W', '<']:
            print("Go West...")
        elif user_action in ['i', 'I', 'INVENTORY']:
            for item in inventory:
                print(f"You have access to the following item: {item}")
        elif user_action in ['Quit', 'quit', 'Q', 'q']:
            print("Safe travels Sailor :D")
            is_user_active = False
        else:
            print("You've doomed us all...")

play()
