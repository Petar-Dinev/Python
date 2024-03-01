def merge(arr, start_index, end_index):
    if start_index < 0:
        start_index = 0
    if end_index >= len(arr):
        end_index = len(arr) - 1
    result = ''
    new_arr = []
    for i in range(len(arr)):
        if i < start_index or i > end_index:
            new_arr.append(arr[i])
        else:
            result += arr[i]
        if i == end_index:
            new_arr.append(result)
    return new_arr


def divide(arr_of_strings, index, partitions):
    word_to_divide = arr_of_strings[index]
    parts_of_word = []
    length_of_parts = int(len(word_to_divide) / partitions)
    for i in range(partitions):
        parts_of_word.append(word_to_divide[0:length_of_parts])
        word_to_divide = word_to_divide[length_of_parts:]
    if word_to_divide:
        parts_of_word[-1] += word_to_divide
    arr_of_strings = arr_of_strings[:index] + parts_of_word + arr_of_strings[index + 1:]

    return arr_of_strings


strings = input().split()
command = input()

while command != '3:1':
    tokens = command.split()
    if tokens[0] == 'merge':
        strings = merge(strings, int(tokens[1]), int(tokens[2]))
    else:
        strings = divide(strings, int(tokens[1]), int(tokens[2]))
    command = input()

print(' '.join(strings))
