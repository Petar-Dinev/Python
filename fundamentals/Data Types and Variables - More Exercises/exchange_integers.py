first_num = int(input())
second_num = int(input())
print('Before:')
print(f'a = {first_num}')
print(f'b = {second_num}')
print('After:')
my_var = second_num
second_num = first_num
first_num = my_var
print(f'a = {first_num}')
print(f'b = {second_num}')
