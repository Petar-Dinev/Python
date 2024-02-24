phones = input().split(', ')
current_line_of_input = input()

while current_line_of_input != 'End':
    command, phone = current_line_of_input.split(' - ')

    if command == 'Add':
        if phone not in phones:
            phones.append(phone)
    elif command == 'Remove':
        if phone in phones:
            phones.remove(phone)
    elif command == 'Bonus phone':
        old_phone, new_phone = phone.split(':')
        if old_phone in phones:
            index_to_insert_new_phone = phones.index(old_phone)
            phones.insert(index_to_insert_new_phone + 1, new_phone)
    elif command == 'Last':
        if phone in phones:
            phones.remove(phone)
            phones.append(phone)

    current_line_of_input = input()

print(', '.join(phones))
