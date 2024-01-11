n = int(input())

for i in range(n):
    current_num = int(input())
    if current_num % 2 != 0:
        print(f'{current_num} is odd!')
        break

else:
    print("All numbers are even.")
