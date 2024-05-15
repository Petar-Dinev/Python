names_count = int(input())
names = set()

for _ in range(names_count):
    current_name = input()
    names.add(current_name)

for name in names:
    print(name)
