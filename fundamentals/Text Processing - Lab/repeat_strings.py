strings = input().split()

result = ''

for string in strings:
    result += len(string) * string

print(result)
