num = int(input())
num_as_string = str(num)
result = ''

for char in num_as_string:
    current_number = int(char)
    current_result = ''
    is_already_added = False
    if len(result) > 0:
        for character in result:
            current_character_in_number = int(character)
            if not is_already_added:
                if current_number > current_character_in_number:
                    current_result += str(current_number)
                    already_added = True
            current_result += str(current_character_in_number)
        if not is_already_added:
            current_result += str(current_number)
        result = current_result
    else:
        result += char

print(result)
