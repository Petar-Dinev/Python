number_of_people = int(input())
capacity_of_elevator = int(input())
courses = 1
while number_of_people > capacity_of_elevator:
    courses += 1
    number_of_people -= capacity_of_elevator

print(courses)
