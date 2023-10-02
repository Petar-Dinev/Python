count_of_tabs = int(input())
salary = float(input())


for num in range(count_of_tabs):
    tab_name = input()

    if tab_name == 'Facebook':
        salary -= 150
    elif tab_name == 'Instagram':
        salary -= 100
    elif tab_name == 'Reddit':
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(int(salary))
