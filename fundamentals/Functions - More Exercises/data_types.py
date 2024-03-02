def check_type(type_of_value, value):
    if type_of_value == 'int':
        return int(value) * 2
    elif type_of_value == 'real':
        result = float(value) * 1.5
        return f"{result:.2f}"
    else:
        return f"${value}$"


type_input = input()
current_value = input()

print(check_type(type_input, current_value))
