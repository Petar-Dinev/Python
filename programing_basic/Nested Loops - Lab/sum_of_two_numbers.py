start = int(input())
end = int(input())
magic_num = int(input())

is_found = False
counter = 0

for num1 in range(start, end + 1):
    for num2 in range(start, end + 1):
        counter += 1
        if num1 + num2 == magic_num:
            is_found = True
            break
    if is_found:
        break

if is_found:
    print(f"Combination N:{counter} ({num1} + {num2} = {magic_num})")
else:
    print(f"{counter} combinations - neither equals {magic_num}")

