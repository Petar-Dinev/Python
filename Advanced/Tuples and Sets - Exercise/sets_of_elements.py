first_set_el_count, second_set_el_count = [int(num) for num in input().split()]

first_set = set()
second_set = set()

for _ in range(first_set_el_count):
    el = input()
    first_set.add(el)

for _ in range(second_set_el_count):
    second_set.add(input())

shared_elements = first_set.intersection(second_set)
print(*shared_elements, sep='\n')
