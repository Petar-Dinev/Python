start_index = int(input())
end_index = int(input())
result = ''
for i in range(start_index, end_index + 1):
    result += f"{chr(i)} "
print(result.rstrip())
