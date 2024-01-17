first_string = input()
second_string = input()

for i in range(len(first_string)):
    current_char_from_first_string = first_string[i]
    current_char_from_second_string = second_string[i]

    current_string = ''
    for k in range(len(first_string)):
        if k == i:
            current_string += current_char_from_second_string
        else:
            current_string += first_string[k]
    first_string = current_string
    if current_char_from_first_string != current_char_from_second_string:
        print(current_string)
