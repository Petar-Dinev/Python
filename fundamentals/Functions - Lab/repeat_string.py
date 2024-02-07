old_string = input()
repeat_count = int(input())

repeat_string_func = lambda x, count: x * count

print(repeat_string_func(old_string, repeat_count))
