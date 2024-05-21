from collections import deque

string = deque(input().split())

main_colors = ['red', 'yellow', 'blue']
secondary_colors = {'orange': ['red', 'yellow'], 'purple': ['red', 'blue'], 'green': ['yellow', 'blue']}
find_colors = []

while string:

    first_part = string.popleft()
    second_part = string.pop() if string else ''

    for color in (first_part + second_part, second_part + first_part):
        if color in main_colors or color in secondary_colors:
            find_colors.append(color)
            break
    else:
        first_part = first_part[:-1]
        second_part = second_part[:-1]
        if first_part:
           string.insert(len(string) // 2, first_part)
        if second_part:
           string.insert(len(string) // 2, second_part)

for color in find_colors:
    if color in secondary_colors:
        for el in secondary_colors[color]:
            if el not in find_colors:
                find_colors.remove(color)

print(find_colors)
