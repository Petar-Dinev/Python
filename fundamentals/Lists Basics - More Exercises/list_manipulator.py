initial_list = [int(num) for num in input().split()]
line = input()

while line != 'end':
    tokens = line.split()
    command = tokens[0]
    if command == 'exchange':
        index_to_split = int(tokens[1])
        if 0 <= index_to_split < len(initial_list):
            first_part_of_list = initial_list[:index_to_split + 1]
            second_part_of_list = initial_list[index_to_split + 1:]
            initial_list = second_part_of_list + first_part_of_list
        else:
            print('Invalid index')
    elif command == 'max':
        type_of_search_num = tokens[1]
        if type_of_search_num == 'odd':
            odd_nums = list(filter(lambda x: x % 2 != 0, initial_list))
            if not odd_nums:
                print('No matches')
            else:
                max_num = max(odd_nums)
                for i in range(len(initial_list) - 1, -1, -1):
                    if initial_list[i] == max_num:
                        print(i)
                        break
        elif type_of_search_num == 'even':
            even_nums = list(filter(lambda x: x % 2 == 0, initial_list))
            if not even_nums:
                print('No matches')
            else:
                max_num = max(even_nums)
                for i in range(len(initial_list) - 1, -1, -1):
                    if initial_list[i] == max_num:
                        print(i)
                        break
    elif command == 'min':
        type_of_search_num = tokens[1]
        if type_of_search_num == 'odd':
            odd_nums = list(filter(lambda x: x % 2 != 0, initial_list))
            if not odd_nums:
                print('No matches')
            else:
                min_num = min(odd_nums)
                for i in range(len(initial_list) - 1, -1, -1):
                    if initial_list[i] == min_num:
                        print(i)
                        break
        elif type_of_search_num == 'even':
            even_nums = list(filter(lambda x: x % 2 == 0, initial_list))
            if not even_nums:
                print('No matches')
            else:
                min_num = min(even_nums)
                for i in range(len(initial_list) - 1, -1, -1):
                    if initial_list[i] == min_num:
                        print(i)
                        break
    elif command == 'first':
        count_of_nums = int(tokens[1])
        type_of_nums = tokens[2]
        if count_of_nums > len(initial_list):
            print('Invalid count')
        else:
            if type_of_nums == 'odd':
                odd_nums = list(filter(lambda x: x % 2 != 0, initial_list))
                print(odd_nums[:count_of_nums])
            else:
                even_nums = list(filter(lambda x: x % 2 == 0, initial_list))
                print(even_nums[:count_of_nums])
    elif command == 'last':
        count_of_nums = int(tokens[1])
        type_of_nums = tokens[2]
        if count_of_nums > len(initial_list):
            print('Invalid count')
        else:
            if type_of_nums == 'odd':
                odd_nums = list(filter(lambda x: x % 2 != 0, initial_list))
                print(odd_nums[-count_of_nums:])
            else:
                even_nums = list(filter(lambda x: x % 2 == 0, initial_list))
                print(even_nums[-count_of_nums:])
    line = input()
print(initial_list)
