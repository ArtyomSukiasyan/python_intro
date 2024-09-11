import random
import string


def generate_password():
    pass_len = get_pass_len()
    preferences = string.ascii_lowercase

    is_prefer_uppercase = get_preference("uppercase")
    if is_prefer_uppercase:
        preferences += string.ascii_letters

    is_prefer_digits = get_preference("digits")
    if is_prefer_digits:
        preferences += string.digits

    return "".join(random.choices(preferences, k=pass_len))


def get_preference(type):
    user_choice = input(f"Do you want {type} (y/n): ")

    return user_choice == "y"


def get_pass_len():
    while True:
        try:
            num = int(input("input password length:  "))

            return num
        except ValueError:
            print("This is not a number.")


print(generate_password())
