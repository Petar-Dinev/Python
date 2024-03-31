spell = input()

line = input()

while line != 'Abracadabra':
    tokens = line.split()
    command = tokens[0]
    if command == 'Abjuration':
        spell = spell.upper()
        print(spell)
    elif command == 'Necromancy':
        spell = spell.lower()
        print(spell)
    elif command == 'Illusion':
        index = int(tokens[1])
        letter = tokens[2]
        if 0 <= index < len(spell):
            spell = spell[:index] + letter + spell[index + 1:]
            print('Done!')
        else:
            print("The spell was too weak.")
    elif command == 'Divination':
        first_substring = tokens[1]
        second_substring = tokens[2]
        if first_substring in spell:
            spell = spell.replace(first_substring, second_substring)
            print(spell)
    elif command == 'Alteration':
        substring = tokens[1]
        if substring in spell:
            spell = spell.replace(substring, '')
            print(spell)
    else:
        print('The spell did not work!')
    line = input()
