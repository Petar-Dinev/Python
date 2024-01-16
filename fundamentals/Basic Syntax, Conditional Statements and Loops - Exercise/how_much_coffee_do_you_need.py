command = input()

need_coffees = 0

while command != 'END':
    if command == 'coding' or command == 'dog' or command == 'cat' or command == 'movie':
        need_coffees += 1
    elif command == 'CODING' or command == 'DOG' or command == 'CAT' or command == 'MOVIE':
        need_coffees += 2
    command = input()

if need_coffees <= 5:
    print(need_coffees)
else:
    print("You need extra sleep")
