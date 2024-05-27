rows, cols = [int(x) for x in input().split()]

matrix = [[el for el in input().split()] for _ in range(rows)]

line = input()

while line != 'END':
    tokens = line.split()

    if 'swap' not in tokens or len(tokens) != 5:
        print('Invalid input!')
        line = input()
        continue

    first_value_row = int(tokens[1])
    first_value_col = int(tokens[2])
    second_value_row = int(tokens[3])
    second_value_col = int(tokens[4])

    if first_value_row not in range(rows) or first_value_col not in range(cols) or second_value_row not in range(rows)\
            or second_value_col not in range(cols):
        print('Invalid input!')
        line = input()
        continue

    matrix[first_value_row][first_value_col], matrix[second_value_row][second_value_col] = \
        matrix[second_value_row][second_value_col], matrix[first_value_row][first_value_col]

    for el in matrix:
        print(*el, sep=' ')

    line = input()
