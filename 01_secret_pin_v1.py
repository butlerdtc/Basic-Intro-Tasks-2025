def secret_pin():
    while True:
        pin = input("Please enter your secret pin: ")
        pin_length = len(pin)
        listed_pin = list(pin)
        if pin_length == 4:
            try:
                for value in listed_pin:
                    int(value)
                break
            except ValueError:
                print("Please only enter numbers")
                pass
        else:
            print("Please enter a 4 digit pin")
    return pin


# Main
secret_pin()