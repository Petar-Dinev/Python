num = int(input())

for current_num in range(1, num + 1):
    is_special = False
    current_num_as_string = str(current_num)
    sum_of_current_num = 0

    for char in current_num_as_string:
        sum_of_current_num += int(char)
    if sum_of_current_num == 5 or sum_of_current_num == 7 or sum_of_current_num == 11:
        is_special = True
    print(f"{current_num} -> {is_special}")
