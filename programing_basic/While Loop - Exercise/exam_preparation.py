bad_grades = int(input())

bad_grades_count = 0
sum_of_all_grades = 0
resolve_task_counter = 0
is_fail = False

command = input()
current_task = ''

while command != 'Enough':
    current_task = command
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades_count += 1
        if bad_grades_count == bad_grades:
            is_fail = True
            break
    resolve_task_counter += 1
    sum_of_all_grades += current_grade
    command = input()

if is_fail:
    print(f"You need a break, {bad_grades} poor grades.")
else:
    avg_grade = sum_of_all_grades / resolve_task_counter
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {resolve_task_counter}")
    print(f"Last problem: {current_task}")
