matrix = [[int(num) for num in input().split()] for _ in range(int(input()))]

prime_diagonal_sum = 0
secondary_diagonal_sum = 0

for row in range(len(matrix)):
    prime_diagonal_sum += matrix[row][row]
    secondary_diagonal_sum += matrix[row][len(matrix) - 1 - row]

print(abs(prime_diagonal_sum - secondary_diagonal_sum))
