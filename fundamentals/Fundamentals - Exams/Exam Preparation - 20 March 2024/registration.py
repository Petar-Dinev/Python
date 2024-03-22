username = input()

line = input()

while line != 'Registration':
    tokens = line.split()
    command = tokens[0]
    if command == 'Letters':
        case = tokens[1]
        if case == 'Lower':
            username = username.lower()
        else:
            username = username.upper()
        print(username)
    elif command == 'Reverse':
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            substring = username[start_index:end_index + 1][::-1]
            print(substring)
    elif command == 'Substring':
        substring = tokens[1]
        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")
    elif command == 'Replace':
        char = tokens[1]
        while char in username:
            username = username.replace(char, '-')
        print(username)
    elif command == 'IsValid':
        char = tokens[1]
        if char in username:
            print('Valid username.')
        else:
            print(f"{char} must be contained in your username.")
    line = input()
