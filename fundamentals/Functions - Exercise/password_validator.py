def validate_password(password):
    length_of_password = len(password)
    is_valid = True
    is_all_chars_alpha_numeric = True
    digits_count = 0

    for char in password:
        if not char.isalnum():
            is_all_chars_alpha_numeric = False
        if char.isdigit():
            digits_count += 1

    if not 6 <= length_of_password <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not is_all_chars_alpha_numeric:
        print("Password must consist only of letters and digits")
        is_valid = False
    if digits_count < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")


input_password = input()

validate_password(input_password)
