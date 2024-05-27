rows, cols = [int(x) for x in input().split()]

matrix = []

start = ord('a')

for row in range(rows):
    current_list = []
    for col in range(cols):
        current_list.append(f"{chr(row + start)}{chr(row + col + start)}{chr(row + start)}")
    matrix.append(current_list)

for el in matrix:
    print(' '.join(el))
