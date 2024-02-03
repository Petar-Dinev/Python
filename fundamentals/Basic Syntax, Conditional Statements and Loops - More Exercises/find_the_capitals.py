string = input()
indexes_of_capital_letters = []

for i in range(len(string)):
    if 65 <= ord(string[i]) <= 90:
        indexes_of_capital_letters.append(i)

print(indexes_of_capital_letters)
        