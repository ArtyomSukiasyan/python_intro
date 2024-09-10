import random


def find_random_number():
    random_number = random.randint(1, 100)

    while True:
        user_input = get_num()

        if user_input > random_number:
            print("Your input is more")
        elif user_input < random_number:
            print("Your input is less")
        else:
            print("You won!")
            return


def get_num():
    while True:
        try:
            num = int(input("input number:  "))

            return num
        except ValueError:
            print("This is not a number.")


find_random_number()
