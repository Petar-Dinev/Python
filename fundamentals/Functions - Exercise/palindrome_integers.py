nums_list = input().split(', ')

for current_num_as_string in nums_list:
    is_palindrome = True
    length_of_current_num_as_string = len(current_num_as_string)
    for i in range(length_of_current_num_as_string // 2):
        if current_num_as_string[i] != current_num_as_string[length_of_current_num_as_string - 1 - i]:
            is_palindrome = False
    print(is_palindrome)
