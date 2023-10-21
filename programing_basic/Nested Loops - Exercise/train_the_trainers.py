jury_count = int(input())
student_avg_grades = 0
count_of_presentations = 0
command = input()

while command != 'Finish':
    presentation = command
    presentation_avg_grade = 0

    for jury in range(jury_count):
        grade = float(input())
        presentation_avg_grade += grade

    presentation_avg_grade /= jury_count
    student_avg_grades += presentation_avg_grade
    count_of_presentations += 1
    print(f"{presentation} - {presentation_avg_grade:.2f}.")
    command = input()

student_avg_grades /= count_of_presentations
print(f"Student's final assessment is {student_avg_grades:.2f}." )