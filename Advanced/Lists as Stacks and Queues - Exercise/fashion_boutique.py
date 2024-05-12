clothes = [int(num) for num in input().split()]
size_of_rack = int(input())

count_of_racks = 0

while clothes:
    count_of_clothes = 0
    while clothes and (count_of_clothes + clothes[-1] <= size_of_rack):
        current_clothes_count = clothes.pop()
        count_of_clothes += current_clothes_count
    count_of_racks += 1
    count_of_clothes = 0

print(count_of_racks)
