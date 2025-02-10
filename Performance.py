# Out to Eat program: 
#   Asks the user a selection/list of types foods that they would like to eat (this will help decide what restaurant they will decide to go to.)
#   Afterwards, they pick the restaurant and get the menu, with the menu in hand they order what they would
# like to eat, after everything is ordered they get the bill, then asked if they would like to buy a dessert after their meal, then are asked to rate the restaurant and if they would like to recommend the program to a friend or not.

# To do list:
#   List of types of foods to decide restaurant (done)
#   List of restaurants (done)
#   Food menu for restaurants (done)
#   Dessert menu after regular food is ordered (done) (to call a 2nd function(look at lastThing.py if confused))
#   Food bill/price
#   Restaurant rating
#   Recommend program

breakfast_diners = ["Ihop", "Denny's", "Waffle House"]

sandwich_shops = ["Subway", "Panera Bread", "Jersey Mike's"]

steakhouses = ["Outback Steakhouse", "Texas Roadhouse", "Chris' Steakhouse"]

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
    if response == "ihop" or "dennys" or "denny's" or "waffle house":
        print(f"Great choice! Here is their menu!: {breakfast_menus}")
    elif response == "subway" or "panera bread" or "jersey mikes" or "jersey mike's":
        print(f"Great choice! Here is their menu!: {sandwich_menu}")
    elif response == "outback steakhouse" or "texas roadhouse" or "chris steakhouse" or "chris' steakhouse":
        print(f"Great choice! Here is their menu!: {steakhouse_menu}")


breakfast_menus = {"Eggs": 3.00,
                   "Bacon": 3.50,
                   "Sausage": 3.50,
                   "Ham": 3.50,
                   "Hash Browns": 3.00,
                   "Biscuit": 2.50,
                   "Toast": 2.25,
                   "French Toast": 3.50,
                   "Pancakes": 3.50,
                   "Waffles": 3.50,
                   "Water": 1.00,
                   "Coffee": 3.00,
                   "Tea": 2.75}

sandwich_menu = {"Lettuce": 2.35,
                 "Cabbage": 2.35,
                 "Tomato": 2.35,
                 "Avocado": 2.65,
                 "Peppers": 2.45,
                 "Onions": 2.45,
                 "Cucumber": 2.45,
                 "Carrot": 2.45,
                 "Spinach": 2.35,
                 "Corn": 2.35,
                 "Mushroom": 2.45,
                 "Water": 1.00,
                 "Juice": 4.50}

steakhouse_menu = {"Steak": 10.50,
                   "Burger": 8.50,
                   "Fries": 4.75,
                   "Soup": 6.75,
                   "Chicken Wings": 7.25,
                   "Baked Potato": 6.00,
                   "Mashed Potato": 5.75,
                   "Shrimp": 8.00,
                   "Turkey": 9.50,
                   "Salmon": 9.00,
                   "Macaroni and Cheese": 6.75}

dessert_menu = {"Cookie": 3.00,
                "Cake Slice": 6.00,
                "Cheesecake slice": 6.00,
                "Brownie": 4.50,
                "Cupcake": 3.50}

# Function to display the stars rating the user gives
def restaurant_rate(rate):
    max_stars = 5 # The maximum amounut of stars for the rating
    print(f"{rate} stars out of {max_stars} stars!")

def start_restaurant_program(program_response):
    if program_response == "no":
        print("Okay suit yourself!")
        return
    
    types_of_foods = ["breakfast", "lunch", "dinner"]

    if program_response == "yes":
        print("Great! Here are my recommendations!")
        type_question = input(f"Do you want to go out to eat for {', '.join(types_of_foods)}?: ").lower()

    restaurant_types(type_question)

# VERY IN PROGRESS / CURRENTLY NOT WORKING LIKE I WANT TO / USE LASTTHING.PY AND USE CONCESSION FUNCTION
    # restaurant_response = input("Which restaurant would you like to go to?: ")
    # restaurant_question(restaurant_response)

start_restaurant_program(program_response = input("Do you want to go out to eat today?: ").lower()) # The user input