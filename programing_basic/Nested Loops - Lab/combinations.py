num = int(input())

counter = 0

for num1 in range(num + 1):
    for num2 in range(num + 1):
        for num3 in range(num + 1):
            if num1 + num2 + num3 == num:
                counter += 1
                
print(counter)
