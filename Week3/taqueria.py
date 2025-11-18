def main():
    # List of all meals
    all_meals = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.75,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    all_meals_items = 0
    while True:
        try:
            # Gets the input from user and make first letter of each word capital
            # and remove every witespace from befor and after inputed text
            item = input("Item: ").title().strip()
            # Check if the text is one of the meals name
            if item in all_meals:
                # Total of prices
                all_meals_items += all_meals[item]
                print(f"Total: ${all_meals_items:.2f}")
            # If user enter anything that is not in the meals list, it will do nothing
            else:
                pass
        # With "ctl + d" the program closes
        except EOFError:
            print()
            break


main()
