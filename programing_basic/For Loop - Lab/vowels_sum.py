word = input()

total_sum = 0

for letter in word:
    if letter == 'a':
        total_sum += 1
    elif letter == 'e':
        total_sum += 2
    elif letter == 'u':
        total_sum += 5
    elif letter == 'i':
        total_sum += 3
    elif letter == 'o':
        total_sum += 4

print(total_sum)
