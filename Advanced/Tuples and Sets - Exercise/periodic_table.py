chemical_elements = set()

for _ in range(int(input())):
    elements = input().split()
    for el in elements:
        chemical_elements.add(el)

print(*chemical_elements, sep="\n")
