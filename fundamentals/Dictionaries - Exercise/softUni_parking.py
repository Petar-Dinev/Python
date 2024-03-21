commands_count = int(input())
guests = {}

for i in range(commands_count):
    line = input()
    tokens = line.split()
    command = tokens[0]
    if command == 'register':
        guest = tokens[1]
        license_number = tokens[2]
        if guest not in guests:
            print(f"{guest} registered {license_number} successfully")
            guests[guest] = license_number
        else:
            print(f"ERROR: already registered with plate number {guests[guest]}")
    else:
        username = tokens[1]
        if username not in guests:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del guests[username]
for guest in guests.keys():
    print(f"{guest} => {guests[guest]}")
