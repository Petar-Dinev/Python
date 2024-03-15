string = input()

fixed_string = ''
current_char = ''

for char in string:
    if char != current_char:
        fixed_string += char
    current_char = char

print(fixed_string)
