from collections import deque

current_water = int(input())
names = deque()
name = input()

while name != 'Start':
    names.append(name)
    name = input()

line = input()
while line != 'End':
    tokens = line.split()
    if len(tokens) == 1:
        need_water = int(tokens[0])
        removed_name = names.popleft()
        if current_water >= need_water:
            current_water -= need_water
            print(f"{removed_name} got water")
        else:
            print(f"{removed_name} must wait")
    else:
        current_water += int(tokens[1])
    line = input()
print(f"{current_water} liters left")
