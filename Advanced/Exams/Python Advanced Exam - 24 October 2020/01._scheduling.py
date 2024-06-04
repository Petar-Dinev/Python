from sys import maxsize
tasks = [int(num) for num in input().split(', ')]
search_task_index = int(input())
total_cycles = 0


while True:
    index = tasks.index(min(tasks))
    if index == search_task_index:
        break
    total_cycles += tasks[index]
    tasks[index] = maxsize

total_cycles += tasks[index]
print(total_cycles)
