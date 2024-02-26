employees = [int(num) for num in input().split()]
happiness_factor = int(input())

employees = list(map(lambda x: x * happiness_factor, employees))
average_happiness = sum(employees) / len(employees)
happy_employees = list(filter(lambda x: x > average_happiness, employees))
happy_employees_count = len(happy_employees)
total_employees = len(employees)

if happy_employees_count >= total_employees / 2:
    print(f"Score: {happy_employees_count}/{total_employees}. Employees are happy!")
else:
    print(f"Score: {happy_employees_count}/{total_employees}. Employees are not happy!")
