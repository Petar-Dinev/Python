number_of_strings = int(input())

for i in range(number_of_strings):
    string = input()

    for k in range(len(string)):
        char = string[k]
        if char == '.' or char == ',' or char == '_':
            print(f"{string} is not pure!")
            break
    else:
        print(f"{string} is pure.")
