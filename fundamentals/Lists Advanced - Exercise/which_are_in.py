first_sequence = input().split(', ')
second_sequence = input().split(', ')
result = []

for first_string in first_sequence:
    for current_sequence in second_sequence:
        if first_string in current_sequence:
            result.append(first_string)
            break

print(result)
