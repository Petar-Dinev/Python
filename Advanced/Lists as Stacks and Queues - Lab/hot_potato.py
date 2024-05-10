from collections import deque

kids = deque(input().split())
rotations = int(input()) - 1

while len(kids) > 1:
    kids.rotate(-rotations)
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids[0]}")
