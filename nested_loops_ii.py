for x in range(1, 5):
    factors = []
    for y in range(1, x + 1):
        if x % y == 0:
            factors.append(y)

    for z in factors:
        print(f"{z} is a factor of {x}")
    print("")
