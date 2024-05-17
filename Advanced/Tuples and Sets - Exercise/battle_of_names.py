names_count = int(input())
odd_set = set()
even_set = set()

for i in range(1, names_count + 1):
    current_name = input()
    current_name_chars_sum = 0

    for char in current_name:
        current_name_chars_sum += ord(char)
    current_name_chars_sum //= i

    if current_name_chars_sum % 2 == 0:
        even_set.add(current_name_chars_sum)
    else:
        odd_set.add(current_name_chars_sum)

odd_set_sum = sum(odd_set)
even_set_sum = sum(even_set)

if odd_set_sum == even_set_sum:
    print(*odd_set.union(even_set), sep=', ')
elif odd_set_sum > even_set_sum:
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')
