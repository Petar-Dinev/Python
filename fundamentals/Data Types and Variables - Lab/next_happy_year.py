current_year = int(input())
is_not_found_happy_year = True

while is_not_found_happy_year:

    current_year += 1
    current_year_as_string = str(current_year)
    count = 0

    for i in range(len(current_year_as_string)):

        current_char = current_year_as_string[i]

        for char in current_year_as_string:
            if current_char == char:
                count += 1

    if count == len(current_year_as_string):
        is_not_found_happy_year = False

print(current_year)
