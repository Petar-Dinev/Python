rows_of_matrix = int(input())

matrix = [list(input()) for _ in range(rows_of_matrix)]
search_symbol = input()

is_found = False

for row in range(rows_of_matrix):
    if search_symbol in matrix[row]:
        for col in range(rows_of_matrix):
            if matrix[row][col] == search_symbol:
                print(f"({row}, {col})")
                is_found = True
                break

    if is_found:
        break

if not is_found:
    print(f"{search_symbol} does not occur in the matrix")
