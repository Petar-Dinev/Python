number = int(input())

for num in range(1111, 10000):
    is_magic = True
    num_in_string = str(num)
    for index in range(len(num_in_string)):
        if int(num_in_string[index]) == 0 or number % int(num_in_string[index]) != 0:
            is_magic = False
            break
    if is_magic:
        print(num, end=" ")
