matrix = []

for _ in range(int(input())):
    matrix.append([int(x) for x in input().split(', ')])

print([num for row in matrix for num in row])
