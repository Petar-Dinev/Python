kid_tickets = 0
standard_tickets = 0
student_tickets = 0

command = input()

while command != 'Finish':
    movie = command
    command2 = input()
    seats = 0
    if command2 != 'End':
        seats = int(command2)
    movie_tickets_sell = 0
    while command2 != 'End':
        type_of_ticket = input()
        if type_of_ticket == 'student':
            student_tickets += 1
            movie_tickets_sell += 1
        elif type_of_ticket == 'standard':
            standard_tickets += 1
            movie_tickets_sell += 1
        elif type_of_ticket == 'kid':
            kid_tickets += 1
            movie_tickets_sell += 1
        if movie_tickets_sell == seats:
            break
        command2 = type_of_ticket
    percent_movie_full_hall = movie_tickets_sell / seats * 100
    print(f"{movie} - {percent_movie_full_hall:.2f}% full.")
    command = input()

total_tickets = kid_tickets + standard_tickets + student_tickets
standard_tickets_percent = standard_tickets / total_tickets * 100
student_tickets_percent = student_tickets / total_tickets * 100
kid_tickets_percent = kid_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets_percent:.2f}% student tickets.")
print(f"{standard_tickets_percent:.2f}% standard tickets.")
print(f"{kid_tickets_percent:.2f}% kids tickets.")
