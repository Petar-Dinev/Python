name = input()

while name != 'Welcome!':
    if name == 'Voldemort':
        print("You must not speak of that name!")
        break
    house_name = ''
    if len(name) < 5:
        house_name = 'Gryffindor'
    elif len(name) == 5:
        house_name = 'Slytherin'
    elif len(name) == 6:
        house_name = 'Ravenclaw'
    else:
        house_name = 'Hufflepuff'
    print(f"{name} goes to {house_name}.")
    name = input()
else:
    print('Welcome to Hogwarts.')
