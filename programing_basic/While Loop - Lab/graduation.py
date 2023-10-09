name_of_student = input()
current_class = 1
total_amount_of_grades = 0
is_Excluded = False
student_fails = 0

while current_class <= 12:
    current_annual_grade = float(input())
    if current_annual_grade < 4:
        student_fails += 1
        if student_fails > 1:
            is_Excluded = True
            break
    else:
        current_class += 1
        total_amount_of_grades += current_annual_grade

if is_Excluded:
    print(f"{name_of_student} has been excluded at {current_class} grade")
else:
    average_grades_amount = total_amount_of_grades / 12
    print(f"{name_of_student} graduated. Average grade: {average_grades_amount:.2f}")