number = int(input())

current_num = 0
is_end = False

for num in range(1, number + 1):
    for num2 in range(num):
        current_num += 1
        if number < current_num:
            is_end = True
            break
        print(f"{current_num}", end=" ")
    print()
    if is_end:
        break


