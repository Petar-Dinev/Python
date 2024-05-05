shopping_list = input().split('!')

line = input()

while line != 'Go Shopping!':
    tokens = line.split()
    command = tokens[0]
    first_product = tokens[1]

    if command == 'Urgent':
       if first_product not in shopping_list:
           shopping_list.insert(0, first_product)
    elif command == 'Unnecessary':
        if first_product in shopping_list:
            shopping_list.remove(first_product)
    elif command == 'Rearrange':
        if first_product in shopping_list:
            shopping_list.remove(first_product)
            shopping_list.append(first_product)
    else:
        second_product = tokens[2]
        if first_product in shopping_list:
            index = shopping_list.index(first_product)
            shopping_list[index] = second_product

    line = input()

print(', '.join(shopping_list))
