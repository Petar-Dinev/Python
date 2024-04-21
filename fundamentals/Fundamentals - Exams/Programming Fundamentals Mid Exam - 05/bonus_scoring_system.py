import math

num_of_students = int(input())
num_of_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_student_attendances = 0

for _ in range(num_of_students):
    current_student_attendances = int(input())
    current_student_bonus = current_student_attendances / num_of_lectures * (5 + additional_bonus)
    if current_student_bonus > max_bonus:
        max_bonus = current_student_bonus
        max_student_attendances = current_student_attendances

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {max_student_attendances} lectures.")
