lines_count = int(input())
longest_intersection = []

for _ in range(lines_count):
    first_set_data, second_set_data = input().split('-')

    first_set_start, first_set_end = [int(x) for x in first_set_data.split(',')]
    second_set_start, second_set_end = [int(x) for x in second_set_data.split(',')]

    first_set = set([num for num in range(first_set_start, first_set_end + 1)])
    second_set = set([num for num in range(second_set_start, second_set_end + 1)])

    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = list(current_intersection)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
