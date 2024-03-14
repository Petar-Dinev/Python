strings = input().split()
total_sum = 0

for string in strings:
    first_letter = string[0]
    last_letter = string[-1]
    num = int(string[1:len(string) - 1])

    if first_letter.isupper():
        num /= (ord(first_letter) - 64)
    else:
        num *= (ord(first_letter) - 96)

    if last_letter.isupper():
        num -= (ord(last_letter) - 64)
    else:
        num += (ord(last_letter) - 96)

    total_sum += num

print(f"{total_sum:.2f}")
