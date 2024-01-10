word = input()

# for i in range(len(word)-1, -1, -1):
#     print(word[i], end="")

result = ''

for i in range(len(word)-1, -1, -1):
    result += word[i]

print(result)
