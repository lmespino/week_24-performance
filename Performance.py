# Out to Eat program: Asks the user a selection/list of types foods that they would like to eat (this will help decide what restaurant they will decide to go to.), afterwards, they pick the restaurant and get the menu, with the menu in hand they order what they would
# like to eat, after everything is order they get the bill, and then are asked to rate the restaurant and if they would like to recommend the restaurant to a friend or not.

# To do list:
#   List of types of foods to decide restaurant
#   List of restaurants
#   Food menu for restaurants
#   Food bill/price
#   Restaurant rating
#   Recommend restaurant

types_of_foods = ["breakfast", "lunch", "dinner"]

breakfast_diners = ["Ihop", "Denny's", "Waffle House"]

sandwich_shops = ["Subway", "Panera Bread", "Jersey Mike's"]

steakhouses = ["Outback Steakhouse", "Texas Roadhouse", "Ruth's Chris Steak House"]

def restaurant_types(type):
    if type == "breakfast":
        print("I recommend going to a diner!")
    if type == "lunch":
        print("I recommend going to a sandwich shop!")
    if type == "dinner":
        print("I recommend going to a steakhouse!")

breakfast_menus = {"Eggs": 2.00,
                   "Bacon": 2.50,
                   "Sausage": 2.50,
                   "Ham": 2.50,
                   "Hash Browns": 2.00,
                   "Biscuit": 1.50,
                   "Toast": 1.25,
                   "French Toast": 2.50,
                   "Pancakes": 2.50,
                   "Waffles": 2.50,
                   "Water": 1.00,
                   "Coffee": 2.00,
                   "Tea": 1.75}

sandwich_menu = {"Lettuce": 1.35,
                 "Cabbage": 1.35,
                 "Tomato": 1.35,
                 "Avocado": 1.65,
                 "Peppers": 1.45,
                 "Onions": 1.45,
                 "Cucumber": 1.45,
                 "Carrot": 1.45,
                 "Spinach": 1.35,
                 "Corn": 1.35,
                 "Mushroom": 1.45,
                 "Water": 1.00,
                 "Juice": 3.50}

steakhouse_menu = {"Steak": 9.50,
                   "Burger": 6.50,
                   "Fries": 4.75}