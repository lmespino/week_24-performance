breakfast_diners = ["Ihop", "Denny's", "Waffle House"] # List of breakfast places

sandwich_shops = ["Subway", "Panera Bread", "Jersey Mike's"] # List of lunch/sandwich shops

steakhouses = ["Outback Steakhouse", "Texas Roadhouse", "Chris' Steakhouse"] # List of dinner/steakhouse places

breakfast_menu = {"eggs": 3.00,
                  "bacon": 3.50,
                  "sausage": 3.50,
                  "ham": 3.50,
                  "hash browns": 3.00,
                  "biscuit": 2.50,
                  "toast": 2.25,
                  "french toast": 3.50,
                  "pancakes": 3.50,
                  "waffles": 3.50,
                  "water": 1.00,
                  "coffee": 3.00,
                  "tea": 2.75}

sandwich_menu = {"lettuce": 2.35,
                 "cabbage": 2.35,
                 "tomato": 2.35,
                 "avocado": 2.65,
                 "peppers": 2.45,
                 "onions": 2.45,
                 "cucumber": 2.45,
                 "carrot": 2.45,
                 "spinach": 2.35,
                 "corn": 2.35,
                 "mushroom": 2.45,
                 "ham": 2.00,
                 "cheese": 1.75,
                 "chicken": 2.00,
                 "salami": 2.25,
                 "turkey": 2.50,
                 "water": 1.00,
                 "juice": 3.50,
                 "soda": 2.50}

steakhouse_menu = {"steak": 10.50,
                   "burger": 8.50,
                   "fries": 4.75,
                   "soup": 6.75,
                   "chicken wings": 7.25,
                   "baked potato": 6.00,
                   "mashed potato": 5.75,
                   "shrimp": 8.00,
                   "turkey": 9.50,
                   "salmon": 9.00,
                   "macaroni and cheese": 6.75,
                   "water": 1.00,
                   "wine": 10.50,
                   "soda": 2.50,}

dessert_menu = {"cookie": 2.50,
                "cake slice": 6.00,
                "cheesecake slice": 6.00,
                "brownie": 4.50,
                "cupcake": 3.50,
                "ice cream": 3.00}

def restaurant_types(type):
    if type == "breakfast":
        print("I recommend going to a diner!")
        print(f"Here are my choices for diners!: {breakfast_diners}")
    if type == "lunch":
        print("I recommend going to a sandwich shop!")
        print(f"Here are my choices for sandwich shops!: {sandwich_shops}")
    if type == "dinner":
        print("I recommend going to a steakhouse!")
        print(f"Here are my choices for steakhouses!: {steakhouses}")

def restaurant_question(response):
    if response == "ihop" or response == "dennys" or response == "denny's" or response == "waffle house":
        print("Great choice! Here is their menu!: ")
        food_bill(breakfast_menu)
    elif response == "subway" or response == "panera bread" or response == "jersey mikes" or response == "jersey mike's":
        print(f"Great choice! Here is their menu!: ")
        food_bill(sandwich_menu)
    elif response == "outback steakhouse" or response == "texas roadhouse" or response == "chris steakhouse" or response == "chris' steakhouse":
        print("Great choice! Here is their menu!: ")
        food_bill(steakhouse_menu)

def food_bill(menu):
    cart = []
    total = 0

    print("--------- MENU ---------")
    for key, value in menu.items():
        print(f"{key:17}: ${value:.2f}")
    print("------------------------")

    while True:
        food = input("Select an item ('stop' to stop ordering): ").lower()
        if food == "stop":
            break
        elif menu.get(food) is not None:
            cart.append(food)
            total += menu.get(food)

    print(f"You ordered: {', '.join(cart)}")
    print()
    print(f"Your total here is: ${total:.2f}")
    print()

def program_rate(recommend_question):
    if recommend_question == "yes":
        print("Thank you very much!")
    elif recommend_question == "no":
        print("Aw, sorry that you didn't like the program")

    max_stars = 5
    star_rating = int(input("What would you like to rate this program? 1 - 5 stars: "))
   
    if star_rating < 1 or star_rating > 5:
        print("That's not a valid number! Please rate between 1 and 5.")
    else:
        print(f"{star_rating} stars out of {max_stars} stars! Thank you!")
   
def start_restaurant_program(program_response):
    if program_response == "no":
        print("Okay, suit yourself!")
        return

    types_of_foods = ["breakfast", "lunch", "dinner"]

    if program_response == "yes":
        print("Great! Here are my recommendations!")
        type_question = input(f"Do you want to go out to eat for {', '.join(types_of_foods)}?: ").lower()

    restaurant_types(type_question)

    restaurant_response = input("Which restaurant would you like to go to?: ").lower()

    restaurant_question(restaurant_response)
   
def program_continuation_dessert(dessert_response):
    if dessert_response == "no":
        print("Okay, suit yourself!")
        return
   
    if dessert_response == "yes":
        print("Great! Here is the dessert menu:")
        food_bill(dessert_menu)

start_restaurant_program(program_response = input("Do you want to go out to eat today?: ").lower())

program_continuation_dessert(dessert_response = input("Would you like to look at the dessert menu?: ").lower())

program_rate(recommend_question = input("Would you like to recommend this program and its functionality to others?: ").lower())