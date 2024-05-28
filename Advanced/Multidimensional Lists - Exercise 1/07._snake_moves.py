from collections import deque

rows, cols = [int(x) for x in input().split()]
string = deque(input())

matrix = []

for row in range(rows):
    current_list = []

    for col in range(cols):
        if row % 2 == 0:
            current_list.append(string[0])
        else:
            current_list.insert(0, string[0])
        string.rotate(-1)

    matrix.append(current_list)

[print(*row, sep='') for row in matrix]
