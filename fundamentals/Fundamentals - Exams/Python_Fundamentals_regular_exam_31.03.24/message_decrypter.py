import re

count_of_lines = int(input())
pattern = r'^([\$\%])([A-Z][a-z]{2,})\1:\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$'

for i in range(count_of_lines):
    line = input()
    match = re.match(pattern, line)
    if match:
        tag = match.group(2)
        first_num = int(match.group(3))
        second_num = int(match.group(4))
        third_num = int(match.group(5))
        message = chr(first_num) + chr(second_num) + chr(third_num)
        print(f'{tag}: {message}')
    else:
        print("Valid message not found!")
