matrix_rows = int(input())

matrix = [[int(num) for num in input().split(', ')] for _ in range(matrix_rows)]

prime_diagonal_nums = []
secondary_diagonal_nums = []

for row in range(matrix_rows):
    prime_diagonal_nums.append(matrix[row][row])
    secondary_diagonal_nums.append(matrix[row][matrix_rows - row - 1])

print(f"Primary diagonal: {', '.join([str(x) for x in prime_diagonal_nums])}. Sum: {sum(prime_diagonal_nums)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal_nums])}. Sum: {sum(secondary_diagonal_nums)}")
