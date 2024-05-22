rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

for col in range(cols):
    current_col_sum = 0

    for row in range(rows):
        current_col_sum += matrix[row][col]

    print(current_col_sum)
