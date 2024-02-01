nums_list = input().split(' ')
string = input()
message = ''

for current_num_as_string in nums_list:
    current_num_sum = 0
    for current_digit_as_string in current_num_as_string:
        current_num_sum += int(current_digit_as_string)
    while current_num_sum >= len(string):
        current_num_sum -= len(string)
    message += string[current_num_sum]
    string = string[:current_num_sum] + string[current_num_sum + 1:]

print(message)
