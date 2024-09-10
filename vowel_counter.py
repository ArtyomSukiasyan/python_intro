def count_vowels_in_str(str):
    is_valid_input = validate_input(str)

    if not is_valid_input:
        return f"The input {str} is not string"

    vowels = "aeoiu"
    count = 0
    
    for char in str:
        if char in vowels:
            count += 1

    return count


def validate_input(input):
    return type(input) == str


str1 = "asddwafa"
str2 = "dfafafaw"
str3 = 1231
str4 = "a1321"
str5 = "1321"
str6 = {"str": "adawda"}

print(count_vowels_in_str(str1))
print(count_vowels_in_str(str2))
print(count_vowels_in_str(str3))
print(count_vowels_in_str(str4))
print(count_vowels_in_str(str5))
print(count_vowels_in_str(str6))
