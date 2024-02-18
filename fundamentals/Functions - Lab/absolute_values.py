def get_abs_value_of_num(num):
    return abs(num)


nums = [float(num) for num in input().split()]
result = list(map(get_abs_value_of_num, nums))
print(result)
