def check_palindrome(str):
    is_valid_input = validate_input(str)

    if not is_valid_input:
        return f"The input {str} is not string"

    for i in range(len(str)):
        if str[i] != str[-i - 1]:
            return f"string {str} is NOT palindrome"

    return f"string {str} is palindrome"


def validate_input(input):
    return type(input) == str


input1 = "asddsa"
input2 = "asdsa"
input3 = "asdsdasda"
input4 = 12
input5 = "12321"

print(check_palindrome(input1))
print(check_palindrome(input2))
print(check_palindrome(input3))
print(check_palindrome(input4))
print(check_palindrome(input5))
