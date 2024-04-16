languages = {}
students = {}

line = input()

while line != 'exam finished':
    tokens = line.split('-')
    students_name = tokens[0]
    language = tokens[1]
    if language == 'banned':
        del students[students_name]
    else:
        points = int(tokens[2])
        if language not in languages:
            languages[language] = 0
        languages[language] += 1
        if students_name not in students:
            students[students_name] = {}
            if language not in students[students_name]:
                students[students_name][language] = 0

        if students[students_name][language] < points:
            students[students_name][language] = points

    line = input()

print("Results:")

for name, info in students.items():
    total_points = 0
    for _, points in info.items():
        total_points += points
    print(f"{name} | {total_points}")

print("Submissions:")
for language in languages:
    print(f"{language} - {languages[language]}")
