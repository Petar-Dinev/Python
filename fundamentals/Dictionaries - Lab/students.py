students = {}

while True:
    command = input()
    if ':' not in command:
        break
    name, id_, course = command.split(':')
    course_name = '_'.join(course.split())
    if course_name not in students.keys():
        students[course_name] = {}
    students[course_name][name] = id_

for course, students_ in students.items():
    if course == command:
        for student in students_.keys():
            print(f"{student} - {students[course][student]}")
