activation_key = input()

while True:
    line = input()
    if line == 'Generate':
        break
    tokens = line.split('>>>')
    command = tokens[0]

    if command == 'Contains':
        substring = tokens[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command == 'Flip':
        type_of_letters = tokens[1]
        start_index = int(tokens[2])
        end_index = int(tokens[3])
        first_part = activation_key[:start_index]
        second_part = activation_key[end_index:]
        string_to_change = activation_key[start_index:end_index]
        if type_of_letters == 'Lower':
            string_to_change = string_to_change.lower()
        else:
            string_to_change = string_to_change.upper()
        activation_key = first_part + string_to_change + second_part
        print(activation_key)
    elif command == 'Slice':
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

print(f"Your activation key is: {activation_key}")
