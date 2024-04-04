strings_count = int(input())

for i in range(strings_count):
    string = input()
    start_name_index = string.index('@') + 1
    end_name_index = string.index('|')
    start_age_index = string.index('#') + 1
    end_age_index = string.index('*')
    name = string[start_name_index:end_name_index]
    age = string[start_age_index:end_age_index]
    print(f"{name} is {age} years old.")
