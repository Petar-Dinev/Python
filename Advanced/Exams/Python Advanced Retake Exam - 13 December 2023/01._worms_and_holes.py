from collections import deque

worms = [int(worm) for worm in input().split()]
holes = deque([int(el) for el in input().split()])

start_worms_count = len(worms)
worms_fit_holes = 0

while worms and holes:
    current_hole = holes.popleft()

    if worms[-1] == current_hole:
        worms_fit_holes += 1
        worms.pop()
    else:
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()

if worms_fit_holes:
    print(f"Matches: {worms_fit_holes}")
else:
    print("There are no matches.")

if worms:
    print(f"Worms left: {', '.join([str(el) for el in worms])}")
else:
    if worms_fit_holes == start_worms_count:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")

if holes:
    print(f"Holes left: {', '.join([str(el) for el in holes])}")
else:
    print("Holes left: none")
