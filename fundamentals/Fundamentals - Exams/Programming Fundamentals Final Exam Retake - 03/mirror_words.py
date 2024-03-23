import re

pattern = r"([@#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"

string_input = input()
matches = re.findall(pattern, string_input)
found_couples = len(matches)

couples = []

for i in range(len(matches)):
    first_word = matches[i][1]
    second_word = matches[i][2]
    second_word_backwards = second_word[::-1]
    if first_word == second_word_backwards:
        couples.append(f'{first_word} <=> {second_word}')

if found_couples:
    print(f'{found_couples} word pairs found!')
else:
    print('No word pairs found!')

if len(couples):
    print('The mirror words are:')
    print(', '.join(couples))
else:
    print('No mirror words!')
