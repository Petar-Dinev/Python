goal_steps = 10000
total_steps = 0
is_fail = False

while total_steps < goal_steps:
    command = input()
    if command == "Going home":
        last_steps = int(input())
        total_steps += last_steps
        if total_steps < goal_steps:
            is_fail = True
            break
    else:
        current_steps = int(command)
        total_steps += current_steps

difference = abs(total_steps - goal_steps)

if is_fail:
    print(f"{difference} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
