def calc_fibonacci(num):
    n1 = 0
    n2 = 1
    nextTerm = 1

    for i in range(1, num):
        nextTerm = n1 + n2
        n1 = n2
        n2 = nextTerm

    return n1


def get_num():
    while True:
        try:
            num = int(input("input number:  "))

            return num
        except ValueError:
            print("This is not a number.")


user_input = get_num()
print(calc_fibonacci(user_input))
