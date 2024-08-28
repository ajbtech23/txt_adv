def get_user_choice():
    return input("What are we buying today Sailor?\n")

def pretty_print(arr_to_print):
    for element in arr_to_print:
        print(f"* {element}")

def even_prettier_print(arr_to_print):
    for i in range(len(arr_to_print)):
        print(f"{i + 1} {arr_to_print[i]}")

def even_prettier_still_print(arr_to_print):
    i = 0
    for element in arr_to_print:
        print(f"{i + 1}... {element}")
        i += 1

arr_sneaker = []

is_customer_still_shopping = True

while is_customer_still_shopping:

    customer_selection = get_user_choice()

    if customer_selection == "":
        print("Back to the cruel mistress of the sea yer go!")
        is_customer_still_shopping = False
    else:
        print(f"Sweet mother of Pearl! That's a fine choice ye make!")
        print(f"I\'ll be adding the {customer_selection} to Davy Jones locker for ya XD")
        arr_sneaker.append(customer_selection)

print("\nApproach 1...")
pretty_print(arr_sneaker)

print("\nApproach 2...")
even_prettier_print(arr_sneaker)

print("\nApproach 3...")
even_prettier_still_print(arr_sneaker)
