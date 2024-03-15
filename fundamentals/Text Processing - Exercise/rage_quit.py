start_string = input()
repetitions = ''
final_string = ''
current_string = ''
for index in range(len(start_string)):
    if not start_string[index].isdigit():
        current_string += start_string[index].upper()
    else:
        for i in range(index, len(start_string)):
            if start_string[i].isdigit():
                repetitions += start_string[i]
            else:
                break
        final_string += current_string * int(repetitions)
        current_string = ''
        repetitions = ''

print(f"Unique symbols used: {len(set(final_string))}")
print(final_string)
