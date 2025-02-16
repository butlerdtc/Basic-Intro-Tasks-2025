def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


def bread_choice(options, title):
    count = 1
    print(f"{title} choices:")
    for option in options:
        print(f"** {count} ** {option[0]}: ${option[1]:.2f}")
        count += 1
    while True:
        choice = integer_checker("Please enter the number of the bread you would "
                             "like: ")
        if 1 <= choice <= 4:
            break
        else:
            print("Please choose one of the options!")
            continue


bread = [["Wholemeal", 1.00], ["White", 0.80], ["Cheesy White", 1.20],
         ["Gluten Free", 1.40]]
meat = [["Chicken", 2.69], ["Beef", 3.00], ["Salami", 4.00], ["Vegan Slice",
                                                              3.30]]
garnish = [["Onion", 1.69], ["Tomato", 1.00], ["Lettuce", 2.00],
           ["Cheese", 2.50]]
bread_choice(bread, "Bread")
print("Exit")