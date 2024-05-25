from sys import maxsize

rows, cols = [int(num) for num in input().split()]

matrix = [[int(num) for num in input().split()] for _ in range(rows)]

biggest_sum = -maxsize
start_point = []

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = 0
        for i in range(3):
            for j in range(3):
                current_sum += matrix[row + i][col + j]
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            start_point = [row, col]

print(f"Sum = {biggest_sum}")
sub_matrix = [el[start_point[1]: start_point[1] + 3] for el in matrix[start_point[0]: start_point[0] + 3]]
for el in sub_matrix:
    print(*el, sep=' ')
