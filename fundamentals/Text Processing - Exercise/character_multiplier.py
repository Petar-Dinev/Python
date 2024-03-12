string_one, string_two = input().split()

lower_length_string = min(len(string_one), len(string_two))
total_sum = 0
index = 0

for i in range(lower_length_string):
    index = i
    total_sum += ord(string_one[i]) * ord(string_two[i])

if lower_length_string == len(string_one):
    for i in range(index + 1, len(string_two)):
        total_sum += ord(string_two[i])
else:
    for i in range(index + 1, len(string_one)):
        total_sum += ord(string_one[i])

print(total_sum)
