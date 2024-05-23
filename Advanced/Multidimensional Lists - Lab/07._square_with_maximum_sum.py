from sys import maxsize

rows, cols = [int(num) for num in input().split(', ')]

matrix = [[int(num) for num in input().split(', ')] for _ in range(rows)]

biggest_sum = -maxsize
sub_matrix_with_biggest_sum = []

for row in range(rows - 1):
    for col in range(cols - 1):

        num1 = matrix[row][col]
        num2 = matrix[row][col + 1]
        num3 = matrix[row + 1][col]
        num4 = matrix[row + 1][col + 1]
        current_sum = num1 + num2 + num3 + num4

        if current_sum > biggest_sum:
            biggest_sum = current_sum
            sub_matrix_with_biggest_sum = [[num1, num2], [num3, num4]]

print(*sub_matrix_with_biggest_sum[0], sep=' ')
print(*sub_matrix_with_biggest_sum[1], sep=' ')
print(biggest_sum)
