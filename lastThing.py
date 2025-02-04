# concession stand program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

menu2 = {"water": 1.25,
        "candy": 2.00,
        'hotdog': 3.50,
        'ice cream': 3.25,
        'coffee': 2.50,
        'tea': 2.25}

def concession(menu):
    cart = []
    total = 0

    print("--------- MENU ---------")
    for key, value in menu.items():
        print(f"{key:10}: ${value:.2f}")
    print("------------------------")

    while True:
        food = input("Select an item (q to quit): ").lower()
        if food == "q":
            break
        elif menu.get(food) is not None:
            cart.append(food)
            total += menu.get(food)

    for food in cart:
        print(food, end=" ")
    print()
    print(f"Total is: ${total:.2f}")

concession(menu)
concession(menu2)