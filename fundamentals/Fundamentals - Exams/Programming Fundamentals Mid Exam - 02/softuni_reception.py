first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())
all_employee_efficiency = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
time = 0

while students_count > 0:
    time += 1
    if time % 4 != 0:
        students_count -= all_employee_efficiency

print(f"Time needed: {time}h.")
