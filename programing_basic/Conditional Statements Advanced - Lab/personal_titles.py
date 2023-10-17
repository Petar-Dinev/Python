age = float(input())
gender = input()

if age < 16:
    if gender == 'f':
        print('Miss')
    else:
        print('Master')
else:
    if gender == 'f':
        print('Ms.')
    else:
        print('Mr.')
