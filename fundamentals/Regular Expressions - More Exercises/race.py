import re

participants_arr = input().split(', ')
participants_dict = {}

for participant in participants_arr:
    participants_dict[participant] = 0

line = input()
# name_pattern = r""
# digit_pattern = r"\d"
pattern = r"\w"

while line != 'end of race':
    name = ''
    kilometers = 0

    characters = re.findall(pattern, line)

    for char in characters:
        if char.isalpha():
            name += char
        elif char.isdigit():
            kilometers += int(char)

    line = input()

    if name in participants_dict:
        participants_dict[name] += kilometers

sorted_participants = sorted(participants_dict.items(), key=lambda x: -x[1])

print(f"1st place: {sorted_participants[0][0]}")
print(f"2nd place: {sorted_participants[1][0]}")
print(f"3rd place: {sorted_participants[2][0]}")
