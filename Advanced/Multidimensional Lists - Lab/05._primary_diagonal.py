lines_of_matrix = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(lines_of_matrix)]

prime_diagonal_sum = 0

for i in range(lines_of_matrix):
    prime_diagonal_sum += matrix[i][i]

print(prime_diagonal_sum)
