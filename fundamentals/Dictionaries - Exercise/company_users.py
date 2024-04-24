companies = {}

line = input()

while line != 'End':
    company, employee = line.split(' -> ')
    if company not in companies:
        companies[company] = []
    if employee not in companies[company]:
        companies[company].append(employee)
    line = input()

for company in companies:
    print(company)
    for employee in companies[company]:
        print(f"-- {employee}")
