def calc_factorial(num):
    fac = 1

    for i in range(2, num + 1):
        fac *= i

    return fac


def calc_factorial_rec(num):
    if num == 1:
        return 1

    return num * calc_factorial_rec(num - 1)


def get_num():
    while True:
        try:
            num = int(input("input number:  "))

            return num
        except ValueError:
            print("This is not a number.")


user_input = get_num()
print(calc_factorial(user_input))
print(calc_factorial_rec(user_input))
