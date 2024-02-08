def print_grade_type(grade):
    type_of_grade = ''

    if 2 <= grade < 3:
        type_of_grade = 'Fail'
    elif 3 <= grade < 3.5:
        type_of_grade = 'Poor'
    elif 3.5 <= grade < 4.5:
        type_of_grade = 'Good'
    elif 4.5 <= grade < 5.5:
        type_of_grade = 'Very Good'
    elif 5.5 <= grade <= 6:
        type_of_grade = 'Excellent'

    print(type_of_grade)


grade_data = float(input())
print_grade_type(grade_data)
