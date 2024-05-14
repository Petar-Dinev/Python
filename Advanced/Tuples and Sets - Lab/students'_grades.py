students_count = int(input())

students = {}

for _ in range(students_count):
    name, grade_as_string = input().split()
    grade = float(grade_as_string)

    if name not in students:
        students[name] = []

    students[name].append(grade)

for student, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    formatted_grades = [f"{grade:.2f}" for grade in grades]
    print(f'{student} -> {" ".join(formatted_grades)} (avg: {avg_grade:.2f})')
