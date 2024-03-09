phonebook = {}
command = input()

while len(command) != 1:
    name, phone_number = command.split('-')
    phonebook[name] = phone_number
    command = input()

for i in range(int(command)):
    search_name = input()
    if search_name in phonebook:
        print(search_name, '->', phonebook[search_name])
    else:
        print(f"Contact {search_name} does not exist.")
