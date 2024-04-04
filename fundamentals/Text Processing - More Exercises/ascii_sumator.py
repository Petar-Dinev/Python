first_character = input()
second_character = input()
string = input()
ascii_sum = 0

for char in string:
    if ord(char) in range(ord(first_character) + 1, ord(second_character)):
        ascii_sum += ord(char)

print(ascii_sum)
