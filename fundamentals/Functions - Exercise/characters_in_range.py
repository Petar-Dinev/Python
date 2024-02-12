first_char = input()
second_char = input()

start_index = ord(first_char) + 1
end_index = ord(second_char)

for i in range(start_index, end_index):
    print(chr(i), end=' ')
