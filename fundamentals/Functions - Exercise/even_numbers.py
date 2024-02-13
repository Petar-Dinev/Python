nums_list = [int(num) for num in input().split()]
even_nums_list = list(filter(lambda x: x % 2 == 0, nums_list))
print(even_nums_list)
