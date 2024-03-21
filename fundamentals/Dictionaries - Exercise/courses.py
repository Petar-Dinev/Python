courses = {}

while True:
    line = input()
    if line == 'end':
        break
    course, student = line.split(' : ')
    if course not in courses:
        courses[course] = []
    courses[course].append(student)

for current_course in courses:
    print(f"{current_course}: {len(courses[current_course])}")
    for student in courses[current_course]:
        print(f"-- {student}")
