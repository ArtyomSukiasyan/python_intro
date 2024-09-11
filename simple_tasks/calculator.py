def calculator():
    first_num = get_num("first")
    second_num = get_num("second")

    return {
        "sum": first_num + second_num,
        "diff": first_num - second_num,
        "multiple": first_num * second_num,
        "divide": first_num / second_num
    }


def get_num(num_count: str):
    while True:
        try:
            num = float(input(f"input {num_count} number:  "))

            return num
        except ValueError:
            print("This is not a number.")


print(calculator())
