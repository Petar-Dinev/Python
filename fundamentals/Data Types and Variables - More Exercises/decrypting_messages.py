key_value = int(input())
num_of_lines = int(input())
message = ''

for i in range(num_of_lines):
    current_char = input()
    message += (chr(ord(current_char) + key_value))

print(message)
