def get_player_command():
    return input('Action: \n')

def play():
    print("Escape from Greed Island -____-!")
    action_input = get_player_command()

    if action_input == 'n' or action_input == 'N' or action_input == 'NAWF':
        print(action_input + " will usher us into our sanctuary - AMEN!")
    elif action_input == 'e' or action_input == 'E' or action_input == 'EASTYYY':
        print(action_input + " salvation lies to the " + action_input + " I SAY!")
    elif action_input == 's' or action_input == 'S' or action_input == 'SOUF':
        print(action_input + " as described in the prophetic by the our great Oracle...")
    elif action_input == 'w' or action_input == 'W' or action_input == 'WEST':
        print(action_input + " promises us great riches like no other!")
    else:
        print("You\'ve doomed us all...")

play()
