arr_triplets = []

while len(arr_triplets) < 3:

    user_food = input("What would you like to add to the cart today?\n")
    arr_triplets.append(user_food)

for good in arr_triplets:
    print(f"We can eat some {good} if we get hungry...")
