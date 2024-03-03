my_list = input().split()
my_dict = {}

for i in range(0, len(my_list), 2):
    my_dict[my_list[i]] = int(my_list[i + 1])

print(my_dict)
