students_count = int(input())
students = {}

for i in range(0, students_count * 2, 2):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

for student in students:
    avg_grade = sum(students[student]) / len(students[student])
    if avg_grade >= 4.5:
        print(f"{student} -> {avg_grade:.2f}")
