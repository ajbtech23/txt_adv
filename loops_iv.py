arr_nba_roster = []

more_players = True

while more_players:
    user_input = input("Who would you like to add to your team?\n")

    if user_input == '':
        print("Your team is now complete!\n")
        more_players = False
    else:
        arr_nba_roster.append(user_input)

i = 0
for player in arr_nba_roster:
    print(f"At the {i + 1} we have {player}")
    i += 1

print("\n")

for player in arr_nba_roster:
    print(f"* {player}")
