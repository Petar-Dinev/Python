sequence = input()
chars_dict = {}

for char in sequence:
    if char != ' ':
        if char not in chars_dict:
            chars_dict[char] = 0
        chars_dict[char] += 1

for key, value in chars_dict.items():
    print(key, '->', value)
