rows = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

bombs = input().split()

for bomb in bombs:
    row, col = [int(index) for index in bomb.split(',')]
    bomb_value = matrix[row][col]

    if bomb_value > 0:
        start_row = row - 1 if row - 1 >= 0 else 0
        end_row = row + 2 if row + 2 <= len(matrix) else len(matrix)
        start_col = col - 1 if col - 1 >= 0 else 0
        end_col = col + 2 if col + 2 <= len(matrix[row]) else len(matrix[row])
        for i in range(start_row, end_row):
            for j in range(start_col, end_col):
                if matrix[i][j] > 0:
                    matrix[i][j] -= bomb_value

alive_cells = 0
cells_sum = 0

for row in matrix:
    for col in row:
        if col > 0:
            alive_cells += 1
            cells_sum += col

print(f"Alive cells: {alive_cells}")
print(f"Sum: {cells_sum}")

[print(*row) for row in matrix]
