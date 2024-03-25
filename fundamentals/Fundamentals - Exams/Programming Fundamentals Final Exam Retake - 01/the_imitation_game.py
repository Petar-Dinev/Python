encrypted_message = input()

line = input()

while line != 'Decode':
    tokens = line.split('|')
    command = tokens[0]
    if command == 'Move':
        number_of_letters = int(tokens[1])
        sequence, left_letters = encrypted_message[:number_of_letters], encrypted_message[number_of_letters:]
        encrypted_message = left_letters + sequence
    elif command == 'Insert':
        index = int(tokens[1])
        value = tokens[2]
        first_part = encrypted_message[:index]
        second_part = encrypted_message[index:]
        encrypted_message = first_part + value + second_part
    elif command == 'ChangeAll':
        substring = tokens[1]
        replacement = tokens[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    line = input()

print(f"The decrypted message is: {encrypted_message}")
