import random

rules = {
    "r": {"name": "rock", "defeats": "s"},
    "p": {"name": "paper", "defeats": "r"},
    "s": {"name": "scissors", "defeats": "p"},
}


def get_user_input():
    while True:
        user_input = input("Choose Rock, Paper or Scissors (r/p/s): ")
        valid_values = "rps"

        if user_input not in valid_values:
            print("Invalid argument, type one of r,p,s")
            continue

        computer_choice = random.choice(valid_values)

        print(get_winner(user_input, computer_choice))


def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw!"

    choice = rules[player_choice]
    if choice["defeats"] == computer_choice:
        return "You won!"

    return "You lost!"


get_user_input()
