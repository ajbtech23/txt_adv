def get_player_action():
    return input("What would you like to do Captain?\n")

def play():

    player_is_active = True
    user_avatar_inventory = ['Dagger', 'Gold(5)', 'Crusty Bread']

    print("Can you escape Greed Island?")
    while player_is_active:

        user_avatar_action = get_player_action()

        if user_avatar_action in ['n', 'N', 'north', 'North', '^']:
            print("We are going North!")
        elif user_avatar_action in ['e', 'E', 'east', 'East', '>']:
            print("We are going East!")
        elif user_avatar_action in ['s', 'S', 'south', 'South', 'v']:
            print("We are going South!")
        elif user_avatar_action in ['w', 'W', 'west', 'West', '<']:
            print("We are going West")
        elif user_avatar_action in ['i', 'I', 'inventory', 'INVENTORY']:
            print("Let's take a look at what we have in our inventory...")
            for item in user_avatar_inventory:
                print(f"You have access to the {item}")
        elif user_avatar_action in ['q', 'Q', 'quit', 'Quit']:
            print("Fare ye well dear Sailor")
            player_is_active = False
        else:
            print("We cyant understand ye matey!")

play()
