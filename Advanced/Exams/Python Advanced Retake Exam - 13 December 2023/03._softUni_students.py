def softuni_students(*args, **kwargs):
    students = {}

    for student_data in args:
        student_id, student_name = student_data
        students[student_name] = student_id

    courses = {}

    for course_id, course_name in kwargs.items():
        courses[course_id] = course_name

    invalid_students = []
    result = []

    for student_name, student_id in sorted(students.items(), key=lambda kvp: kvp[0]):
        if student_id in courses:
            result.append(f"*** A student with the username {student_name} has successfully \
finished the course {courses[student_id]}!")
        else:
            invalid_students.append(student_name)

    if invalid_students:
        result.append(f"!!! Invalid course students: {', '.join(invalid_students)}")

    return '\n'.join(result)


print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))

