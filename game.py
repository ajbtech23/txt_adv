print("Escape from Greed Island -___-")
action_input = input('Action: ')
print(action_input + " because the only way is up!")

if action_input == 'n':
    print("Go north!")
elif action_input == 'e':
    print("Go East!")
elif action_input == 's':
    print("Go South!")
elif action_input == 'w':
    print("Go West!")
else:
    print("Invalid action XD")

print("Escape from Cave Terror")
action_input = input("Quickly! Where to next?!\n")
if action_input == 'n' or action_input == 'N':
    print("North! We must go North!")
elif action_input == 'e' or action_input == 'E':
    print("East! Our future lies to the East!!!")
elif action_input == 's' or action_input == 'S':
    print("Sur! We must go to the South or perish in the Great Fire...")
elif action_input == 'w' or action_input == 'W':
    print("The sun sets in the West - we must go West for safe passage")
else:
    print("Your indecision has cost us everything")
