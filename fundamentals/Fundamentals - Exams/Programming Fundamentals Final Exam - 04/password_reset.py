password = input()

command = input()

while command != 'Done':
    tokens = command.split()

    if tokens[0] == 'TakeOdd':
        new_password = ''
        for i in range(len(password)):
            if i % 2 != 0:
                new_password += password[i]
        password = new_password
        print(password)
    elif tokens[0] == 'Cut':
        index = int(tokens[1])
        length = int(tokens[2])
        first_part_of_pass = password[0:index]
        second_part_of_pass = password[index + length:]
        password = first_part_of_pass + second_part_of_pass
        print(password)
    elif tokens[0] == 'Substitute':
        match = tokens[1]
        replacer = tokens[2]
        if match in password:
            while match in password:
                password = password.replace(match, replacer)
            print(password)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {password}")
