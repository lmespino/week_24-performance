# Out to eat / Restaurant program
breakfast_diners = ["Ihop", "Denny's", "Waffle House"] # List of breakfast places

sandwich_shops = ["Subway", "Panera Bread", "Jersey Mike's"] # List of lunch/sandwich shops

steakhouses = ["Outback Steakhouse", "Texas Roadhouse", "Chris' Steakhouse"] # List of dinner/steakhouse places

# The menu for breakfast places
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

# The menu for lunch/sandwich places
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

# The menu for dinner/steakhouse places                
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

# The dessert menu for every place
dessert_menu = {"cookie": 2.50,
                "cake slice": 6.00,
                "cheesecake slice": 6.00,
                "brownie": 4.50,
                "cupcake": 3.50,
                "ice cream": 3.00}

# Function to tell the user the restaurant recommendations from their choice of restaurant type
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

# Function to show the menu of the restaurant the user chose
def restaurant_question(response):
    if response == "ihop" or response == "dennys" or response == "denny's" or response == "waffle house":
        print("Great choice! Here is their menu!: ")
        food_bill(breakfast_menu) # This only shows the breakfast menu if the user chose a diner to eat at
    elif response == "subway" or response == "panera bread" or response == "jersey mikes" or response == "jersey mike's":
        print(f"Great choice! Here is their menu!: ")
        food_bill(sandwich_menu) # This only shows the lunch menu if the user chose a sandwich place to eat at
    elif response == "outback steakhouse" or response == "texas roadhouse" or response == "chris steakhouse" or response == "chris' steakhouse":
        print("Great choice! Here is their menu!: ")
        food_bill(steakhouse_menu) # This only shows the dinner menu if the user chose a steakhouse place to eat at

# Function that displays the menu to user chose, and calculates their total and shows what items they had ordered
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

# Function to display the stars rating the user gives and asks the user if they would recommend this program
def program_rate(recommend_question):
    if recommend_question == "yes": # Only displays if the user says yes to recommending the program
        print("Thank you very much!")
    elif recommend_question == "no": # Only displays if the user says no to recommending the program
        print("Aw, sorry that you didn't like the program")

    max_stars = 5  # The maximum amount of stars for the rating
    star_rating = int(input("What would you like to rate this program? 1 - 5 stars: ")) # Asks the user how many stars they would rate the program out of
   
    if star_rating < 1 or star_rating > 5:
        print("That's not a valid number! Please rate between 1 and 5.") # If the user gives an invalid number it tells them to input a correct one
    else:
        print(f"{star_rating} stars out of {max_stars} stars! Thank you!") # Displays the user's star rating out of the max amount of stars for the program
   
    # Function to start the beginning of the restaurant program
def start_restaurant_program(program_response):
    # The program ends here if the user decides to not use the program
    if program_response == "no":
        print("Okay, suit yourself!")
        return

    # The list of types of foods the user can go out to eat at
    types_of_foods = ["breakfast", "lunch", "dinner"]
   
    # The program continues here if the user says yes
    # The program then asks the types of foods that it currently has available
    if program_response == "yes":
        print("Great! Here are my recommendations!")
        type_question = input(f"Do you want to go out to eat for {', '.join(types_of_foods)}?: ").lower()
   
    # Displays the restaurants available for the user to go to, depending on what type they selected
    restaurant_types(type_question)

    # Asks the user which restaurant they would like to go to from the selection they were given
    restaurant_response = input("Which restaurant would you like to go to?: ").lower()
   
    # This takes the users response and then displays the restaurant's menu they have chosen
    restaurant_question(restaurant_response)
   
    # Function to continue the restaurant program but this asks the user if they would like to look at the desert menu
def program_continuation_dessert(dessert_response):
    # This function ends here if the user decides to not look at the dessert menu
    if dessert_response == "no":
        print("Okay, suit yourself!")
        return
   
    # This displays the dessert menu if the user says yes
    if dessert_response == "yes":
        print("Great! Here is the dessert menu:")
        food_bill(dessert_menu)

start_restaurant_program(program_response = input("Do you want to go out to eat today?: ").lower()) # The user decides if they would like to start the program or not

program_continuation_dessert(dessert_response = input("Would you like to look at the dessert menu?: ").lower()) # The user decides if they would like to see the dessert menu or not

program_rate(recommend_question = input("Would you like to recommend this program and its functionality to others?: ").lower()) # The user decides if they would like to recommend the program to others and asks what rating they would like to give