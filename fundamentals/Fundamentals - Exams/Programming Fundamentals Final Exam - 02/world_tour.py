string = input()

line = input()

while line != 'Travel':
    tokens = line.split(':')
    command = tokens[0]
    if command == 'Add Stop':
        index = int(tokens[1])
        substring = tokens[2]
        if 0 <= index < len(string):
            string = string[:index] + substring + string[index:]
    elif command == 'Remove Stop':
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        if 0 <= start_index < len(string) and 0 <= end_index < len(string):
            string = string[:start_index] + string[end_index + 1:]
    elif command == 'Switch':
        old_string = tokens[1]
        new_string = tokens[2]
        if old_string in string:
            string = string.replace(old_string, new_string)
    print(string)
    line = input()

print(f"Ready for world tour! Planned stops: {string}")
