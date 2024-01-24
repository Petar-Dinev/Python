num = int(input())
start_char_code = 97
for i in range(num):
    for n in range(num):
        for k in range(num):
            print(f'{chr(start_char_code + i)}{chr(start_char_code + n)}{chr(start_char_code + k)}')
