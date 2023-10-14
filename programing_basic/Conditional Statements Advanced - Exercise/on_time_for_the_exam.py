hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrive = int(input())
minutes_of_arrive = int(input())

exam_minutes = hour_of_exam * 60 + minutes_of_exam
arrive_minutes = minutes_of_arrive + hour_of_arrive * 60

difference = abs(exam_minutes - arrive_minutes)

if exam_minutes >= arrive_minutes:
    if difference == 0:
        print('On time')
    elif difference <= 30:
        print('On time')
        print(f'{difference} minutes before the start')
    elif difference > 30:
        print('Early')
        if difference < 60:
            print(f'{difference} minutes before the start')
        else:
            hours = difference // 60
            minutes = difference % 60
            print(f"{hours}:{minutes:02d} hours before the start")
else:
    print('late')
    if difference < 60:
        print(f"{difference} minutes after the start")
    else:
        hours = difference // 60
        minutes = difference % 60
        print(f"{hours}:{minutes:02d} hours after the start")
