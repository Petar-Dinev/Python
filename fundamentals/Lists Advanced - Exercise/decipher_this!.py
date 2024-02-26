encoded_message = input().split()
decoded_message = []

for word in encoded_message:
    first_letter_as_num = ''
    rest_of_word = ''
    for char in word:
        if char.isdigit():
            first_letter_as_num += char
        else:
            rest_of_word += char
    first_letter_as_string = chr(int(first_letter_as_num))

    if len(rest_of_word) > 1:
        rest_of_word = rest_of_word[-1] + rest_of_word[1:-1] + rest_of_word[0]
    decoded_message.append(first_letter_as_string + rest_of_word)

print(' '.join(decoded_message))
