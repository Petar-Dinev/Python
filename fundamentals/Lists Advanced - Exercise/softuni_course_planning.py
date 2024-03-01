course_lessons = input().split(', ')
line = input()

while line != 'course start':
    tokens = line.split(':')
    command = tokens[0]
    lesson = tokens[1]

    if command == 'Add':
        if lesson not in course_lessons:
            course_lessons.append(lesson)
    elif command == 'Insert':
        index = int(tokens[2])
        if lesson not in course_lessons:
            course_lessons.insert(index, lesson)
    elif command == 'Remove':
        if lesson in course_lessons:
            course_lessons.remove(lesson)
    elif command == 'Swap':
        second_lesson = tokens[2]
        if lesson in course_lessons and second_lesson in course_lessons:
            first_lesson_index = course_lessons.index(lesson)
            second_lesson_index = course_lessons.index(second_lesson)
            course_lessons[first_lesson_index], course_lessons[second_lesson_index] = \
                course_lessons[second_lesson_index], course_lessons[first_lesson_index]
            if f"{lesson}-Exercise" in course_lessons:
                first_lesson_exercise = course_lessons.pop(first_lesson_index + 1)
                course_lessons.insert(second_lesson_index + 1, first_lesson_exercise)
            if f"{second_lesson}-Exercise" in course_lessons:
                second_lesson_exercise = course_lessons.pop(second_lesson_index + 1)
                course_lessons.insert(first_lesson_index + 1, second_lesson_exercise)
    elif command == 'Exercise':
        if lesson not in course_lessons:
            course_lessons.append(lesson)
        lesson_index = course_lessons.index(lesson)
        exercise = f"{lesson}-Exercise"
        if exercise not in course_lessons:
            course_lessons.insert(lesson_index + 1, exercise)

    line = input()

for i in range(1, len(course_lessons) + 1):
    print(f"{i}.{course_lessons[i - 1]}")
