def get_critical_values_in_list(values):
    error = validate_values(values)

    if error:
        return error

    return {
        "max value": max(values),
        "min value": min(values),
        "average": sum(values) / len(values)
    }


def validate_values(values):
    if (type(values) != list):
        return "The values is not list type"

    invalid_values = []
    for el in values:
        if type(el) != int:
            invalid_values.append(el)

    if len(invalid_values):
        return f"Invalid elements: {invalid_values}"

    return ""


valid_list = [1, 4, 3, -4, 2, 3, 4, 5, 6, 9, 7, 8]
invalid_list = [1, 4, 3, -4, 2, True, 3, False, 4, "asd", 5, 6, 9, 7, 8]
another_type = (1, 2, 3)

print(get_critical_values_in_list(valid_list))
print(get_critical_values_in_list(invalid_list))
print(get_critical_values_in_list(another_type))
