message = input()

line = input()

while line != 'Reveal':
    tokens = line.split(':|:')
    command = tokens[0]

    if command == 'InsertSpace':
        index = int(tokens[1])
        message = message[:index] + ' ' + message[index:]
        print(message)
    elif command == 'Reverse':
        substring = tokens[1]
        if substring in message:
            index = message.index(substring)
            first_part_of_message = message[:index + len(substring)]
            second_part_of_message = message[index + len(substring):]
            substring = substring[::-1]
            message = first_part_of_message + second_part_of_message + substring
