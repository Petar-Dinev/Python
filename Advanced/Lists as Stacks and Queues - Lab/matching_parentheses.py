expression = input()
result = []
starts_index = []

for i in range(len(expression)):
    if expression[i] == '(':
        starts_index.append(i)
    if expression[i] == ")":
        end_index = i
        start_index = starts_index.pop()
        result.append(expression[start_index:end_index + 1])

print('\n'.join(result))


