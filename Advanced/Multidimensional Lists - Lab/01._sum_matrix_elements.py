rows, cols = [int(num) for num in input().split(', ')]

matrix = []
sum_of_nums = 0

for row in range(rows):
    row_data = [int(num) for num in input().split(', ')]
    sum_of_nums += sum(row_data)
    matrix.append(row_data)

print(sum_of_nums)
print(matrix)
