text = input()
encrypted_text = ''

for char in text:
    current_char_ascii_value = ord(char)
    encrypted_text += chr(current_char_ascii_value + 3)

print(encrypted_text)
