num_as_list = input().split('.')
num_as_string = ''.join(num_as_list)
num_as_number = int(num_as_string)
current_version_as_num = num_as_number + 1
current_version_as_string = str(current_version_as_num)
final_current_version = f'{current_version_as_string[0]}.{current_version_as_string[1]}.{current_version_as_string[2]}'

print(final_current_version)
